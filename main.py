import requests, smtplib, socket, random, time, os
from email.message import EmailMessage
from faker import Faker

fake = Faker()
video_name = "evidence.mp4"
target_number = "+967777449083"
EMAILS_TO_USE = 2
REPORTS_PER_EMAIL = 3

SMTP_SERVER = "mail.smtp2go.com"
SMTP_PORT = 2525
SMTP_USER = "demo@example.com"
SMTP_PASS = "demo_pass"

def generate_complaint(name, email):
    options = [
        f"{target_number} is using my email {email} illegally.",
        f"Identity theft report: {target_number} using {email}.",
        f"This number ({target_number}) is impersonating me. Email: {email}."
    ]
    return random.choice(options)

def generate_temp_email():
    res = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
    return res.json()[0] if res.status_code == 200 else fake.email()

def send_report(fake_email, fake_name):
    msg = EmailMessage()
    msg['Subject'] = "🚨 URGENT Abuse Report"
    msg['From'] = fake_email
    msg['To'] = "support@support.whatsapp.com"
    msg.set_content(generate_complaint(fake_name, fake_email))
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(SMTP_USER, SMTP_PASS)
            smtp.send_message(msg)
            print(f"[✔] Sent: {fake_email}")
    except Exception as e:
        print(f"[✘] Error: {e}")

def launch_blackintel():
    for i in range(EMAILS_TO_USE):
        email = generate_temp_email()
        name = fake.name()
        for j in range(REPORTS_PER_EMAIL):
            send_report(email, name)
            time.sleep(random.randint(2, 5))

launch_blackintel()
