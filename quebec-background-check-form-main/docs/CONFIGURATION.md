# Configuration Guide for Quebec Background Check Form App

## GitHub Integration Configuration

### Step 1: Create GitHub Repository
1. Go to GitHub and create a new repository for storing PDFs
2. Make note of the repository name (e.g., "your-username/pdf-storage")

### Step 2: Generate Personal Access Token
1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Give it a descriptive name like "PDF Form App"
4. Select the following scopes:
   - `repo` (Full control of private repositories)
5. Click "Generate token"
6. **Important**: Copy the token immediately as you won't see it again

### Step 3: Configure Backend
1. Set environment variables on your deployment platform:
   ```bash
   GITHUB_TOKEN=your_personal_access_token_here
   GITHUB_REPO=your-username/pdf-storage
   ```

2. Uncomment the GitHub integration code in `src/routes/pdf_handler.py`:
   ```python
   # Change this line:
   # from src.github_uploader import GitHubUploader
   # To this:
   from src.github_uploader import GitHubUploader
   
   # And change this line:
   # github_result = {"success": False, "error": "GitHub upload disabled for deployment"}
   # To this:
   uploader = GitHubUploader()
   github_result = uploader.upload_pdf_from_bytes(pdf_bytes, unique_filename)
   ```

3. Install PyGithub dependency:
   ```bash
   pip install PyGithub
   ```

## Email Integration Configuration

### Step 1: Choose Email Service
You can use any SMTP service. Popular options:
- **Gmail**: smtp.gmail.com (port 587)
- **Outlook**: smtp-mail.outlook.com (port 587)
- **SendGrid**: smtp.sendgrid.net (port 587)
- **Mailgun**: smtp.mailgun.org (port 587)

### Step 2: Get SMTP Credentials
For Gmail:
1. Enable 2-factor authentication on your Google account
2. Generate an "App Password" for the application
3. Use your Gmail address and the app password

### Step 3: Configure Environment Variables
Set these environment variables:
```bash
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_USE_TLS=true
```

### Step 4: Update Email Configuration
The email configuration is already set up in `email_sender.py`. Just ensure your environment variables are properly configured.

## Deployment with Configuration

### Option 1: Environment Variables in Deployment
Most deployment platforms allow you to set environment variables:

1. **Heroku**: Use `heroku config:set GITHUB_TOKEN=your_token`
2. **Vercel**: Add environment variables in the dashboard
3. **Railway**: Set environment variables in the project settings
4. **DigitalOcean App Platform**: Configure environment variables in the app spec

### Option 2: Configuration File
Create a `.env` file (don't commit to git):
```bash
GITHUB_TOKEN=your_personal_access_token
GITHUB_REPO=your-username/pdf-storage
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SMTP_USE_TLS=true
```

Then load it in your application:
```python
from dotenv import load_dotenv
load_dotenv()
```

## Testing Configuration

### Test GitHub Integration
1. Fill out the form and generate a PDF
2. Check your GitHub repository for the uploaded file
3. Verify the file is properly named with timestamp

### Test Email Integration
1. Fill out the form with a test email
2. Generate and submit the PDF
3. Check xcorelegacy@gmail.com for the email with PDF attachment

## Security Considerations

1. **Never commit secrets** to your repository
2. **Use environment variables** for all sensitive configuration
3. **Rotate tokens regularly** for better security
4. **Use app passwords** instead of main account passwords
5. **Limit token permissions** to only what's needed

## Troubleshooting

### GitHub Issues
- **401 Unauthorized**: Check if your token is valid and has correct permissions
- **404 Not Found**: Verify the repository name is correct
- **403 Forbidden**: Ensure the token has `repo` scope

### Email Issues
- **Authentication Failed**: Check username/password and enable app passwords
- **Connection Timeout**: Verify SMTP server and port settings
- **TLS Errors**: Ensure TLS is properly configured for your email provider

### General Issues
- **CORS Errors**: Ensure the backend allows requests from your frontend domain
- **Environment Variables**: Verify all required variables are set correctly
- **Dependencies**: Make sure all required packages are installed