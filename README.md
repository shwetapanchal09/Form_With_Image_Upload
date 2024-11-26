
# Flask Form Submission with Image Upload and Email Confirmation

This Flask application allows users to submit a form with personal details (name, email, phone, city) and an image. The form submission triggers an email to the user's provided email address with their submitted details and a link to view the uploaded image.

## Features

- Users can fill out a form with their name, email, phone, city, and upload an image.
- The image is saved in the `uploads` folder on the server.
- An email is sent to the user with their submitted information and a link to view the uploaded image.
- The app uses Gmail's SMTP server to send emails.

## Requirements

- Python 3.x
- Flask
- werkzeug
- smtplib (Python standard library)

### Install Dependencies

To install the required dependencies, use the following command:

```bash
pip install Flask werkzeug
```

## Folder Structure

```plaintext
project-directory/
│
├── app.py                # Main Flask application
├── templates/
│   └── form.html         # HTML form for submission
├── uploads/              # Directory where images will be saved
├── README.md             # Project documentation
```

## Setup and Configuration

1. **Upload Folder**: The uploaded images will be stored in a folder named `uploads`. Ensure this folder exists or will be created automatically by the application.

2. **Gmail SMTP Configuration**: To send emails using Gmail, you need to set up an app password if you're using 2-factor authentication with your Google account. Replace `your-email@gmail.com` and `your-app-password` with your Gmail email and app password in the `app.py`:

   ```python
   server.login('your-email@gmail.com', 'your-app-password')
   ```

   To create an app password:
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" as the app and "Windows Computer" as the device (or any other device).
   - Copy the generated password and use it in your app.

3. **Flask App Setup**:
   - Set the Flask app to run in debug mode for development.
   - The form uses the `/submit` route for POST requests to handle the submission.

## Running the Application

To run the application, navigate to the project directory and use the following command:

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000/` (default Flask host and port).

## How It Works

1. When you visit the root URL (`/`), the `form.html` page is rendered with the fields for the user to fill out.
2. The user submits the form with their personal details and image.
3. Upon submission:
   - The image is saved to the `uploads` folder.
   - An email is sent to the user with a confirmation message and a link to the uploaded image.
4. The user is shown a success message with the uploaded image's filename and email confirmation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask for creating the web framework
- Gmail SMTP for email sending functionality
```

### Notes:
1. **Gmail SMTP**: The app sends emails through Gmail's SMTP server. Ensure you have set up an app password (if using 2-factor authentication with Gmail) and replaced the credentials in `app.py`.
   
2. **Uploads Directory**: The `uploads` folder is automatically created when the app runs for the first time, but you can also manually create it if needed.

3. **Template Structure**: Your `form.html` is located inside the `templates/` folder to follow Flask's default template structure. Ensure the HTML form correctly points to the `/submit` route for processing.

This `README.md` should help users understand the functionality of your app, how to set it up, and how it works.