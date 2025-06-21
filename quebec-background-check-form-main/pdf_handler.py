from flask import Blueprint, request, jsonify
from flask_cors import CORS
import base64
import os
import datetime
# from src.github_uploader import GitHubUploader
from src.email_sender import EmailSender

pdf_bp = Blueprint("pdf", __name__)

@pdf_bp.route("/upload_pdf", methods=["POST"])
def upload_pdf():
    data = request.get_json()
    if not data or "pdf_data" not in data:
        return jsonify({"error": "No PDF data provided"}), 400

    pdf_data_base64 = data["pdf_data"]
    from_name = data.get("from_name", "Unknown")
    from_email = data.get("from_email", "unknown@example.com")
    message = data.get("message", "")
    pdf_filename = data.get("pdf_filename", "form.pdf")

    # Decode the base64 PDF data
    try:
        pdf_bytes = base64.b64decode(pdf_data_base64)
    except Exception as e:
        return jsonify({"error": "Invalid PDF data"}), 400

    # Create a unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_filename = f"{timestamp}_{pdf_filename}"

    # Save PDF temporarily for GitHub upload
    temp_pdf_path = f"/tmp/{unique_filename}"
    try:
        with open(temp_pdf_path, "wb") as f:
            f.write(pdf_bytes)
    except Exception as e:
        return jsonify({"error": "Failed to save PDF"}), 500

    # GitHub upload disabled for deployment
    github_result = {"success": False, "error": "GitHub upload disabled for deployment"}

    # Send email notification
    email_result = {"success": False, "error": "Email sending not configured"}
    try:
        email_sender = EmailSender()
        email_result = email_sender.send_pdf_notification(
            to_email="xcorelegacy@gmail.com",
            from_name=from_name,
            from_email=from_email,
            message=message,
            pdf_data=pdf_bytes,
            pdf_filename=unique_filename
        )
        
        if not email_result["success"]:
            print(f"Email sending failed: {email_result['error']}")
            
    except Exception as e:
        print(f"Email sending error: {str(e)}")
        email_result = {"success": False, "error": str(e)}

    # Clean up temporary file
    try:
        os.remove(temp_pdf_path)
    except:
        pass

    # Prepare response
    response_data = {
        "message": "PDF processed successfully! (GitHub upload disabled, email requires configuration)",
        "filename": unique_filename,
        "from_name": from_name,
        "from_email": from_email,
        "github_upload": github_result,
        "email_sent": email_result
    }

    return jsonify(response_data), 200