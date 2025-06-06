from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Contact
from listings.models import Listing
from .email_utils import send_inquiry_notification, send_admin_notification

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = get_object_or_404(Listing, pk=listing_id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        realtor_email = listing.realtor.email
        
        # Check if user is logged in
        if request.user.is_authenticated:
            # Check if user has already made inquiry for this listing
            if Contact.objects.filter(listing=listing, user=request.user).exists():
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('listings:listing', listing_id)
            
            contact = Contact(
                listing=listing,
                user=request.user,
                name=name,
                email=email,
                phone=phone,
                message=message
            )
        else:
            # For non-logged-in users, check by email
            if Contact.objects.filter(listing=listing, email=email).exists():
                messages.error(request, 'An inquiry for this listing has already been made with this email address')
                return redirect('listings:listing', listing_id)
            
            contact = Contact(
                listing=listing,
                user=None,
                name=name,
                email=email,
                phone=phone,
                message=message
            )
        
        contact.save()
        
        # Send email notifications
        try:
            email_sent = send_inquiry_notification(contact, listing)
            admin_email_sent = send_admin_notification(contact, listing)
            
            if email_sent:
                messages.success(request, f'Your inquiry for {listing.title} has been submitted successfully! Our realtor will get back to you soon.')
            else:
                messages.success(request, f'Your inquiry for {listing.title} has been submitted successfully! Our realtor will get back to you soon.')
                messages.warning(request, 'Note: There was an issue sending email notifications, but your inquiry was saved.')
        except Exception as e:
            # Log the error (in production, use proper logging)
            print(f"Email sending failed: {str(e)}")
            messages.success(request, f'Your inquiry for {listing.title} has been submitted successfully! Our realtor will get back to you soon.')
            messages.warning(request, 'Email notifications are temporarily unavailable, but your inquiry was saved.')
        
        return redirect('listings:listing', listing_id)
    else:
        return redirect('pages:index')

@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    
    # Ensure the contact belongs to the logged-in user
    if contact.user != request.user:
        raise Http404("Contact not found")
    
    listing_title = contact.listing.title
    contact.delete()
    messages.success(request, f'Your inquiry for "{listing_title}" has been deleted successfully!')
    return redirect('accounts:dashboard')

@login_required
def edit_contact_message(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    
    # Ensure the contact belongs to the logged-in user
    if contact.user != request.user:
        raise Http404("Contact not found")
    
    if request.method == 'POST':
        new_message = request.POST.get('message', '').strip()
        if new_message:
            contact.message = new_message
            contact.save()
            messages.success(request, f'Your message for "{contact.listing.title}" has been updated successfully!')
        else:
            messages.error(request, 'Message cannot be empty.')
        return redirect('accounts:dashboard')
    
    # For GET requests, still redirect to dashboard (shouldn't happen with modal)
    return redirect('accounts:dashboard')
