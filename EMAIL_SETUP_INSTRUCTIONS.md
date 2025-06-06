# Email Setup Instructions for Production

## Gmail SMTP Configuration

Your Django application is now configured to send emails via Gmail SMTP. Follow these steps to complete the setup:

### 1. Enable 2-Factor Authentication on Gmail
- Go to your Google Account settings
- Enable 2-Factor Authentication if not already enabled

### 2. Generate App Password
- Go to Google Account Settings > Security
- Under "2-Step Verification", find "App passwords"
- Generate a new app password for "Mail" or "Other (custom name)"
- Copy the 16-character app password (no spaces)

### 3. Update Environment Variables
Edit your `.env` file and replace the placeholder values:

```
EMAIL_HOST_USER = your-actual-email@gmail.com
EMAIL_HOST_PASSWORD = your-16-character-app-password
```

### 4. Alternative Email Providers

#### SendGrid
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

#### Mailgun
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'postmaster@your-domain.mailgun.org'
EMAIL_HOST_PASSWORD = 'your-mailgun-password'
```

#### Microsoft Outlook/Hotmail
```python
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### 5. Testing Email Configuration

After updating your credentials, test the email functionality:

1. Start your Django server: `python manage.py runserver`
2. Submit a property inquiry through the website
3. Check your email inbox for notifications

### 6. Troubleshooting

**Common Issues:**
- **Authentication Error**: Check if 2FA is enabled and app password is correct
- **Connection Refused**: Check firewall settings or try port 465 with SSL
- **Rate Limiting**: Gmail has sending limits; consider professional email services for high volume

**Debug Mode:**
To switch back to console emails for debugging:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

### 7. Production Considerations

For production deployment:
- Use environment variables for all sensitive data
- Consider using professional email services (SendGrid, Mailgun, AWS SES)
- Implement email logging and monitoring
- Set up proper error handling and fallbacks

### 8. Current Email Flow

When a property inquiry is submitted:
1. **Realtor Notification**: Email sent to the property's assigned realtor
2. **Client Confirmation**: Thank you email sent to the person making inquiry
3. **Admin Alert**: Notification sent to admin email address

All emails use professional HTML templates with property and contact details.
