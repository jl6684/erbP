from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contact
from listings.models import Listing

# Create your views here.
@login_required
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = get_object_or_404(Listing, pk=listing_id)
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
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
        
        contact.save()
        
        messages.success(request, f'Your inquiry for {listing.title} has been submitted successfully!')
        return redirect('listings:listing', listing_id)
    else:
        return redirect('pages:index')
