from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings

class Command(BaseCommand):
    help = 'Test email configuration by sending a test email'

    def add_arguments(self, parser):
        parser.add_argument(
            '--to',
            type=str,
            help='Email address to send test email to',
            required=True
        )

    def handle(self, *args, **options):
        recipient_email = options['to']
        
        try:
            send_mail(
                subject='Test Email from BC Real Estate',
                message='This is a test email to verify your email configuration is working correctly.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                html_message='''
                <html>
                <body>
                    <h2>Email Configuration Test</h2>
                    <p>This is a test email to verify your email configuration is working correctly.</p>
                    <p><strong>From:</strong> BC Real Estate System</p>
                    <p><strong>Status:</strong> ✅ Email system is working!</p>
                </body>
                </html>
                ''',
                fail_silently=False,
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Test email sent successfully to {recipient_email}!')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to send test email: {str(e)}')
            )
            self.stdout.write(
                self.style.WARNING('Please check your email configuration in settings.py and .env file')
            )
