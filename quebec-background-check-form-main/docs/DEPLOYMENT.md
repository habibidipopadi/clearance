# Deployment Guide

## Frontend-Only Deployment (Recommended for Quick Start)

### GitHub Pages (Simplest Option)

1. **Fork or Clone this Repository**
   ```bash
   git clone https://github.com/habibidipopadi/quebec-background-check-form.git
   ```

2. **Push to Your GitHub Repository**
   ```bash
   cd quebec-background-check-form
   git remote set-url origin https://github.com/YOUR-USERNAME/quebec-background-check-form.git
   git push -u origin main
   ```

3. **Enable GitHub Pages**
   - Go to your repository Settings
   - Navigate to "Pages" section
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"

4. **Access Your Site**
   - Your site will be available at: `https://YOUR-USERNAME.github.io/quebec-background-check-form/`
   - It may take a few minutes to deploy

### Netlify (Alternative Frontend Hosting)

1. **Deploy with Drag & Drop**
   - Visit [Netlify Drop](https://app.netlify.com/drop)
   - Drag your project folder containing `index.html`
   - Your site will be instantly deployed

2. **Deploy from GitHub**
   - Log in to [Netlify](https://www.netlify.com/)
   - Click "New site from Git"
   - Connect your GitHub account
   - Select your repository
   - Deploy settings:
     - Build command: (leave empty)
     - Publish directory: `/`
   - Click "Deploy site"

### Vercel (Another Alternative)

1. **Deploy from GitHub**
   - Log in to [Vercel](https://vercel.com/)
   - Click "New Project"
   - Import your GitHub repository
   - Framework Preset: "Other"
   - Click "Deploy"

## Full Stack Deployment (With Backend)

### Railway

1. **Prepare Your Repository**
   - Ensure all files are committed
   - Create a `Procfile` in the root:
     ```
     web: python main.py
     ```

2. **Deploy to Railway**
   - Visit [Railway](https://railway.app/)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Python and deploy

3. **Configure Environment Variables**
   - In Railway dashboard, go to "Variables"
   - Add:
     ```
     SENDER_EMAIL=your-email@gmail.com
     SENDER_PASSWORD=your-app-password
     GITHUB_TOKEN=your-github-token
     GITHUB_REPO=your-username/pdf-storage
     ```

### Heroku

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew install heroku/brew/heroku
   
   # Windows
   # Download installer from heroku.com
   ```

2. **Prepare Your App**
   ```bash
   cd quebec-background-check-form
   heroku create your-app-name
   ```

3. **Add Buildpack**
   ```bash
   heroku buildpacks:set heroku/python
   ```

4. **Configure Environment Variables**
   ```bash
   heroku config:set SENDER_EMAIL=your-email@gmail.com
   heroku config:set SENDER_PASSWORD=your-app-password
   heroku config:set GITHUB_TOKEN=your-github-token
   heroku config:set GITHUB_REPO=your-username/pdf-storage
   ```

5. **Deploy**
   ```bash
   git push heroku main
   ```

### DigitalOcean App Platform

1. **Create App**
   - Log in to [DigitalOcean](https://www.digitalocean.com/)
   - Go to "Apps" → "Create App"
   - Choose GitHub as source
   - Select your repository

2. **Configure App**
   - Type: Web Service
   - Environment Variables:
     ```
     SENDER_EMAIL=your-email@gmail.com
     SENDER_PASSWORD=your-app-password
     GITHUB_TOKEN=your-github-token
     GITHUB_REPO=your-username/pdf-storage
     ```
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `python main.py`

3. **Deploy**
   - Click "Next" and "Create Resources"
   - Your app will be deployed automatically

## Post-Deployment Steps

### 1. Add PDF Template
**Important**: The application requires the Quebec Background Check PDF template:
- Obtain `Provincial consent form.pdf` from official sources
- For GitHub Pages: Add to repository and commit
- For other platforms: Upload through deployment platform's file manager

### 2. Test Your Deployment
1. Visit your deployed URL
2. Toggle between English/French
3. Fill out a test form
4. Generate PDF (will fail without template)
5. Test email functionality (if backend deployed)

### 3. Update Email Recipient
If needed, update the email recipient in the code:
- Frontend: Search for `correctionalfacilities@aa87.org`
- Backend: Update in `pdf_handler.py`

### 4. Monitor Your App
- Check deployment logs for errors
- Monitor GitHub repository for uploaded PDFs
- Verify emails are being received

## Troubleshooting Common Issues

### PDF Template Not Found
- Ensure `Provincial consent form.pdf` is in the same directory as `index.html`
- Check file permissions
- Verify exact filename match

### CORS Errors
- Frontend and backend on different domains
- Solution: Update CORS settings in `main.py`

### Email Not Sending
- Check environment variables
- Verify SMTP credentials
- Check spam folder
- Review server logs

### GitHub Upload Failing
- Verify token has correct permissions
- Check repository exists
- Ensure token hasn't expired

## Performance Optimization

### Frontend
- Minify HTML, CSS, JavaScript
- Optimize images
- Enable browser caching
- Use CDN for libraries

### Backend
- Use production WSGI server (Gunicorn)
- Enable response compression
- Implement rate limiting
- Add health check endpoint

## Security Recommendations

1. **HTTPS Only**
   - Always use HTTPS in production
   - Redirect HTTP to HTTPS

2. **Environment Variables**
   - Never commit secrets
   - Rotate credentials regularly

3. **Input Validation**
   - Validate all form inputs
   - Sanitize file uploads
   - Limit file sizes

4. **Rate Limiting**
   - Prevent abuse
   - Limit form submissions per IP

5. **Error Handling**
   - Don't expose sensitive errors
   - Log errors securely
   - Provide user-friendly messages