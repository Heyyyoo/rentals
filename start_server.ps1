# PowerShell script to start Django server with email environment variables
# This ensures the email password is set before starting the server

Write-Host "Setting email environment variables..." -ForegroundColor Green
$env:EMAIL_HOST_USER = "june85933@gmail.com"
$env:EMAIL_HOST_PASSWORD = "inwwlwyhwywfsziv"

Write-Host "Email configuration:" -ForegroundColor Green
Write-Host "  EMAIL_HOST_USER: $env:EMAIL_HOST_USER"
Write-Host "  EMAIL_HOST_PASSWORD: [HIDDEN]"

Write-Host "`nStarting Django development server..." -ForegroundColor Green
Write-Host "Server will be available at http://127.0.0.1:8000/" -ForegroundColor Yellow
Write-Host "Press Ctrl+C to stop the server`n" -ForegroundColor Yellow

# Navigate to project root and start server
cd ..
python manage.py runserver

