# Outlook Email Configuration Issues & Solutions

## Issue with Outlook.com
Microsoft has disabled basic SMTP authentication for outlook.com accounts, which is why you're getting the "basic authentication is disabled" error.

## Solution Options:

### 1. Gmail (Easiest)
- Switch to Gmail with app passwords
- Update your .env file with Gmail credentials
- Gmail still supports app passwords for SMTP

**Steps:**
1. Create/use a Gmail account
2. Enable 2-Factor Authentication
3. Generate an App Password
4. Update .env file

### 2. Microsoft 365/Business Outlook
If you have a Microsoft 365 business account:
```python
EMAIL_HOST = 'smtp.office365.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### 3. Professional Email Services (Production Ready)

#### SendGrid
```python
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = 'your-sendgrid-api-key'
```

#### Mailgun
```python
EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'postmaster@your-domain.mailgun.org'
EMAIL_HOST_PASSWORD = 'your-mailgun-password'
```

#### AWS SES
```python
EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-aws-smtp-username'
EMAIL_HOST_PASSWORD = 'your-aws-smtp-password'
```

## Current Recommendation:
Use Gmail for development/testing, then switch to a professional service for production.

## Gmail Setup Instructions:
1. Go to Google Account Settings
2. Enable 2-Factor Authentication
3. Go to App Passwords section
4. Generate password for "Mail"
5. Use the 16-character password in your .env file
