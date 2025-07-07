import smtplib
import random
from email.mime.text import MIMEText

EMAIL_ADDRESS = "hopeandme08@gmail.com"  # 🔁 your Gmail here
EMAIL_PASSWORD = "acbyxvqeonrczpgg"  # 🔁 your 16-char app password

def generate_otp():
    return str(random.randint(100000, 999999))

def send_email_otp(to_email, otp):
    msg = MIMEText(f"Your RMAS OTP code is: {otp}")
    msg['Subject'] = "RMAS OTP Verification"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
