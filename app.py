from flask import Flask, render_template, request, url_for, send_from_directory
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()
# Define the folder to save uploaded images
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Serve the 'uploads' directory as a static folder
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    user_email = request.form['email']
    phone = request.form['phone']
    city = request.form['city']

    # Check if an image file is part of the form submission
    if 'image' not in request.files:
        return "No image part in the form"
    
    image = request.files['image']
    
    # Check if the file has a name (meaning the user selected a file)
    if image.filename == '':
        return "No selected file"
    
    # Save the image file securely
    image_filename = secure_filename(image.filename)
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
    image.save(image_path)

    # Generate a URL to access the uploaded image
    image_url = url_for('uploaded_file', filename=image_filename, _external=True)

    # Construct the email message to be sent to the user's email
    msg = MIMEMultipart()
    msg['From'] = os.getenv('email')  # Your email address
    msg['To'] = user_email  # Send to the email provided by the user in the form
    msg['Subject'] = 'Form Submission Confirmation'

    # Email body with the submitted information and the image link
    body = f"""
    Hi {name},

    Thank you for submitting your details. Here are the details you provided:

    Name: {name}
    Email: {user_email}
    Phone: {phone}
    City: {city}

    You can view the image you uploaded by clicking the link below:
    {image_url}

    Regards,
    Your Company
    """
    msg.attach(MIMEText(body, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv('email'), os.getenv('password'))  # Your email and app-specific password
        server.send_message(msg)
        server.quit()
        return f"Form submitted successfully, and email sent! Image saved as: {image_filename}"
    except Exception as e:
        return f"Failed to send email: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
