# Email Configuration Setup Guide

## Gmail SMTP Configuration

The email feature has been configured to send rental request notifications to **june85933@gmail.com**.

### Important: Gmail App Password Required

To send emails through Gmail, you need to use an **App Password** (not your regular Gmail password). Follow these steps:

### Step 1: Enable 2-Factor Authentication
1. Go to your Google Account settings: https://myaccount.google.com/
2. Navigate to **Security**
3. Enable **2-Step Verification** if not already enabled

### Step 2: Generate App Password
1. Go to: https://myaccount.google.com/apppasswords
2. Select **Mail** as the app
3. Select **Other (Custom name)** as the device
4. Enter "Django Car Rental" as the name
5. Click **Generate**
6. Copy the 16-character password (it will look like: `abcd efgh ijkl mnop`)

### Step 3: Set Environment Variables

#### For Windows (PowerShell):
```powershell
$env:EMAIL_HOST_USER = "june85933@gmail.com"
$env:EMAIL_HOST_PASSWORD = "inww lwyh wywf sziv"
```

#### For Windows (Command Prompt):
```cmd
set EMAIL_HOST_USER=june85933@gmail.com
set EMAIL_HOST_PASSWORD=your-16-character-app-password
```

#### For Linux/Mac:
```bash
export EMAIL_HOST_USER="june85933@gmail.com"
export EMAIL_HOST_PASSWORD="inww lwyh wywf sziv"
```

### Step 4: Test the Configuration

After setting the environment variables, restart your Django development server and test by submitting a rental request.

### Note
- The email will be sent **from** the Gmail account specified in `EMAIL_HOST_USER` (defaults to june85933@gmail.com)
- The email will be sent **to** june85933@gmail.com (as configured in `ADMIN_EMAIL`)
- Make sure to remove spaces from the App Password when setting it

### Troubleshooting

If emails are not sending:
1. Verify 2-Factor Authentication is enabled
2. Verify the App Password is correct (no spaces)
3. Check that environment variables are set correctly
4. Check Django server logs for error messages
5. Ensure Gmail account has "Less secure app access" is not needed (App Passwords are the secure way)

