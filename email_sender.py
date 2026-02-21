import smtplib
from email.mime.text import MIMEText
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
from datetime import datetime

def send_email():
    # Set up email server
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    port = 587  # For starttls
    sender_email = 'your_email@example.com'  # Replace with your email
    receiver_email = 'recipient@example.com'  # Replace with recipient email
    password = 'your_password'  # Replace with your email password

    # Prepare the email content
    subject = 'Daily RBI Updates'
    body = 'Here are the summarized RBI updates for today...'  # Replace with actual updates
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())

# Schedule the email to be sent every day at 6 AM IST
scheduler = BlockingScheduler()
scheduler.add_job(send_email, 'cron', hour=6, minute=0, timezone=pytz.timezone('Asia/Kolkata'))

if __name__ == '__main__':
    scheduler.start()