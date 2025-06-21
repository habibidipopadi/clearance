# Quebec Background Check Form

## 🚀 Live Demo
Check out the live application: [Quebec Background Check Form](https://habibidipopadi.github.io/quebec-background-check-form/)

## 📋 Overview
A bilingual (English/French) digital form application for Quebec correctional facilities volunteer screening. This web application allows users to complete background check forms digitally, with features including:

- ✅ Complete bilingual form interface
- ✅ Digital signature capability
- ✅ Government ID photo upload
- ✅ PDF generation with embedded photos
- ✅ Direct email functionality
- ✅ Mobile-responsive design

## 🌟 Features

### Form Sections
1. **Involvement Information**
   - Sobriety date tracking
   - Multiple involvement options
   - Bridging the Gap (BTG) specific fields

2. **Personal Information**
   - Full name fields with character limits
   - Date of birth
   - Gender selection
   - Mother's full name

3. **Contact Information**
   - Complete address fields
   - Multiple phone numbers with validation
   - Email address
   - Postal code formatting

4. **Background Information**
   - Criminal history questions
   - Conditional detail fields

5. **Document Upload**
   - Government-issued ID photo upload
   - File size and format validation

6. **Consent & Signature**
   - Digital signature canvas
   - Date stamping
   - Consent acknowledgment

### Technical Features
- **Language Toggle**: Seamless English/French switching
- **Form Validation**: Real-time field validation
- **Phone Number Formatting**: Canadian phone number auto-formatting
- **Character Counters**: Visual feedback for text limits
- **PDF Generation**: Client-side PDF creation with embedded photos
- **Email Integration**: Direct submission to correctional facilities

## 🛠️ Technology Stack

### Frontend
- HTML5, CSS3, JavaScript (Vanilla)
- PDF-lib for PDF generation
- Canvas API for digital signatures
- Responsive design with CSS Grid/Flexbox

### Backend (Optional)
- Python Flask API
- SQLAlchemy for database
- CORS support
- Email/GitHub integration capabilities

## 📦 Installation

### Quick Start (Frontend Only)
1. Clone the repository:
   ```bash
   git clone https://github.com/habibidipopadi/quebec-background-check-form.git
   cd quebec-background-check-form
   ```

2. Open `index.html` in a web browser or serve with any HTTP server:
   ```bash
   # Using Python
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   ```

### Full Installation (With Backend)
1. Clone and setup:
   ```bash
   git clone https://github.com/habibidipopadi/quebec-background-check-form.git
   cd quebec-background-check-form
   
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python main.py
   ```

3. Access at `http://localhost:5000`

## ⚠️ Important: Missing PDF Template

The application requires the official Quebec Background Check PDF template file:
- **Required file**: `Provincial consent form.pdf`
- **Location**: Place in the same directory as `index.html`
- **Source**: Obtain from Quebec correctional facilities or government website

Without this file, the PDF generation will fail. The application will show an error message if the template is missing.

## 📧 Configuration

### Email Configuration (Backend Required)
To enable email functionality:

1. Set environment variables:
   ```bash
   export SENDER_EMAIL="your-email@gmail.com"
   export SENDER_PASSWORD="your-app-password"
   export SMTP_SERVER="smtp.gmail.com"
   export SMTP_PORT="587"
   ```

2. Configure the recipient email in the code (default: `correctionalfacilities@aa87.org`)

### GitHub Storage (Optional)
For automatic PDF storage on GitHub:

1. Create a GitHub personal access token
2. Set environment variables:
   ```bash
   export GITHUB_TOKEN="your-token"
   export GITHUB_REPO="username/repo-name"
   ```

## 🚀 Deployment

### GitHub Pages (Frontend Only)
1. Fork this repository
2. Go to Settings → Pages
3. Select "Deploy from branch" → main → root
4. Your site will be available at `https://[username].github.io/quebec-background-check-form/`

### Full Deployment (With Backend)
Deploy to platforms like:
- Heroku
- Railway
- DigitalOcean
- AWS/Azure

Ensure you set all required environment variables on your deployment platform.

## 📱 Usage Guide

1. **Select Language**: Use the toggle switch to choose English or French
2. **Fill the Form**: Complete all required fields (marked with *)
3. **Upload ID**: Select your government-issued ID photo
4. **Sign Digitally**: Use mouse or touch to sign in the signature box
5. **Generate PDF**: Click to create your completed form
6. **Download/Email**: Save the PDF or email it directly

## 🔧 Troubleshooting

### Common Issues
1. **"PDF template not found"**
   - Ensure `Provincial consent form.pdf` is in the correct location
   - Check file permissions

2. **Signature not working**
   - Enable JavaScript in your browser
   - Try using a different browser
   - On mobile, ensure you're using touch events

3. **Email not sending**
   - Backend configuration required
   - Check SMTP credentials
   - Verify firewall settings

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👏 Acknowledgments

- Quebec Correctional Facilities for form requirements
- AA87 organization for volunteer coordination
- PDF-lib team for the excellent PDF generation library

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Contact: correctionalfacilities@aa87.org

---

**Note**: This application is designed for official use by Quebec correctional facilities volunteer programs. Please ensure you have proper authorization before using this form for official submissions.