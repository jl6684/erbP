from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
import logging

logger = logging.getLogger(__name__)

def send_inquiry_notification(contact, listing):
    """
    Send email notification to realtor when a new inquiry is made
    """
    try:
        # Email to realtor
        realtor_subject = f'New Property Inquiry - {listing.title}'
        realtor_context = {
            'contact': contact,
            'listing': listing,
            'inquiry_type': 'New Inquiry'
        }
        
        # Render HTML email template
        realtor_html_message = render_to_string('emails/inquiry_notification.html', realtor_context)
        realtor_plain_message = strip_tags(realtor_html_message)
        
        # Send email to realtor
        send_mail(
            subject=realtor_subject,
            message=realtor_plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[listing.realtor.email],
            html_message=realtor_html_message,
            fail_silently=False,
        )
        
        # Send confirmation email to client (if they provided an email)
        if contact.email:
            client_subject = f'Thank you for your inquiry - {listing.title}'
            client_context = {
                'contact': contact,
                'listing': listing,
                'realtor': listing.realtor
            }
            
            client_html_message = render_to_string('emails/inquiry_confirmation.html', client_context)
            client_plain_message = strip_tags(client_html_message)
            
            send_mail(
                subject=client_subject,
                message=client_plain_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[contact.email],
                html_message=client_html_message,
                fail_silently=False,
            )
        
        logger.info(f'Inquiry notification emails sent for listing {listing.id}')
        return True
        
    except Exception as e:
        logger.error(f'Failed to send inquiry notification emails: {str(e)}')
        return False

def send_admin_notification(contact, listing):
    """
    Send email notification to admin for new inquiries
    """
    try:
        subject = f'Admin Alert: New Property Inquiry - {listing.title}'
        context = {
            'contact': contact,
            'listing': listing,
            'realtor': listing.realtor
        }
        
        html_message = render_to_string('emails/admin_notification.html', context)
        plain_message = strip_tags(html_message)
        
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
            html_message=html_message,
            fail_silently=True,  # Don't fail if admin email fails
        )
        
        logger.info(f'Admin notification sent for listing {listing.id}')
        return True
        
    except Exception as e:
        logger.error(f'Failed to send admin notification: {str(e)}')
        return False
