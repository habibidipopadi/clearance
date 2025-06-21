import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

class EmailSender:
    def __init__(self, smtp_server=None, smtp_port=None, email=None, password=None):
        """
        Initialize email sender
        
        Args:
            smtp_server: SMTP server address
            smtp_port: SMTP server port
            email: Sender email address
            password: Sender email password or app password
        """
        self.smtp_server = smtp_server or os.getenv('SMTP_SERVER', 'smtp.gmail.com')
        self.smtp_port = smtp_port or int(os.getenv('SMTP_PORT', '587'))
        self.email = email or os.getenv('SENDER_EMAIL')
        self.password = password or os.getenv('SENDER_PASSWORD')
        
        if not self.email or not self.password:
            raise ValueError("Email credentials are required. Set SENDER_EMAIL and SENDER_PASSWORD environment variables.")
    
    def send_email_with_attachment(self, to_email, subject, body, attachment_path=None, attachment_data=None, attachment_filename=None):
        """
        Send email with optional PDF attachment
        
        Args:
            to_email: Recipient email address
            subject: Email subject
            body: Email body text
            attachment_path: Path to attachment file (optional)
            attachment_data: Attachment data as bytes (optional)
            attachment_filename: Name for the attachment (required if using attachment_data)
            
        Returns:
            dict: Send result with status and details
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.email
            msg['To'] = to_email
            msg['Subject'] = subject
            
            # Add body to email
            msg.attach(MIMEText(body, 'plain'))
            
            # Add attachment if provided
            if attachment_path and os.path.exists(attachment_path):
                with open(attachment_path, "rb") as attachment:
                    part = MIMEApplication(attachment.read(), _subtype="pdf")
                    part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(attachment_path)}')
                    msg.attach(part)
            elif attachment_data and attachment_filename:
                part = MIMEApplication(attachment_data, _subtype="pdf")
                part.add_header('Content-Disposition', f'attachment; filename= {attachment_filename}')
                msg.attach(part)
            
            # Create SMTP session
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()  # Enable security
            server.login(self.email, self.password)
            
            # Send email
            text = msg.as_string()
            server.sendmail(self.email, to_email, text)
            server.quit()
            
            return {
                "success": True,
                "message": f"Email sent successfully to {to_email}"
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def send_pdf_notification(self, to_email, from_name, from_email, message, pdf_data, pdf_filename):
        """
        Send PDF notification email to xcorelegacy@gmail.com
        
        Args:
            to_email: Recipient email (should be xcorelegacy@gmail.com)
            from_name: Name of the person submitting the form
            from_email: Email of the person submitting the form
            message: Additional message from the submitter
            pdf_data: PDF file data as bytes
            pdf_filename: Name of the PDF file
            
        Returns:
            dict: Send result
        """
        subject = f"New Quebec Background Check Form Submission from {from_name}"
        
        body = f"""
Hello,

You have received a new Quebec Background Check Form submission.

Submitter Details:
- Name: {from_name}
- Email: {from_email}
- Additional Message: {message if message else 'None'}

The completed form is attached as a PDF file.

Best regards,
Quebec Background Check Form System
        """.strip()
        
        return self.send_email_with_attachment(
            to_email=to_email,
            subject=subject,
            body=body,
            attachment_data=pdf_data,
            attachment_filename=pdf_filename
        )