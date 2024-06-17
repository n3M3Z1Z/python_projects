# Import nessesary moduls
import smtplib
import importlib
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
import logging

# Function to install missing modules
def install_and_import(package):
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

# Install required modules
required_modules = ['smtplib', 'email', 'datetime', 'logging']
for module in required_modules:
    install_and_import(module)

# Set up logging
logging.basicConfig(filename='phishing_log.txt', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Set up the MIME
def send_phishing_email(sender_email, sender_password, receiver_email, subject, body, tracking_image_path=None):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

# Attach the body with the msg instance
    message.attach(MIMEText(body, 'html'))

# Attach tracking image if provided
    if tracking_image_path:
        try:
            with open(tracking_image_path, 'rb') as img:
                msg_image = MIMEImage(img.read())
                msg_image.add_header('Content-ID', '<tracking_image>')
                message.attach(msg_image)
        except Exception as e:
            logging.error(f"Failed to attach tracking image. Error: {str(e)}")

# Create the SMTP session for sending the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # use Gmail with port
        server.starttls()  # enable security
        server.login(sender_email, sender_password)  # login with mail_id and password
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        logging.info(f"Email sent to {receiver_email} successfully.")
    except Exception as e:
        logging.error(f"Failed to send email. Error: {str(e)}")

# Example dynamic content
def generate_dynamic_content(username):
    body = f"""
    <html>
    <body>
    <p>Dear {username},</p>
    <p>We have detected unusual activity on your account. Please update your password immediately by clicking the link below:</p>
    <p><a href='http://example.com'>Update Password</a></p>
    <img src="cid:tracking_image" alt="Tracking Image" style="display:none"/>
    <p>Thank you,<br>Security Team</p>
    </body>
    </html>
    """
    return body

# Usage:
sender_email = "youremail@gmail.com"
sender_password = "yourpassword"
receiver_email = "targetemail@example.com"
subject = "Important Security Update"
username = "TargetUser"
tracking_image_path = "tracking_image.png"  # Path to your tracking image

body = generate_dynamic_content(username)
send_phishing_email(sender_email, sender_password, receiver_email, subject, body, tracking_image_path)
