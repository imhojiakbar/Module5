import requests
import smtplib
from passwords import password
from email.message import EmailMessage

def send_request(url):
    data = requests.get(url).json()
    return data

def send_email_function(send_email, receiver_emails, password, subject, content):
    server = "smtp.gmail.com"
    msg = EmailMessage()
    msg["FROM"] = send_email
    msg["TO"] = receiver_emails
    msg["Subject"] = subject
    msg.set_content(content)
    with smtplib.SMTP_SSL(server, 465) as server:
        server.login(send_email, password)
        server.send_message(msg)
        print("Email Sent {0}".format(" ".join(receiver_emails)))

if __name__ == '__main__':
    data = send_request('https://www.boredapi.com/api/activity')
    sender = "khojiakbarme04"
    password = password
    with open("email.list.py") as f:
        emails = [email.strip() for email in f.readlines()]
    body = data["activity"]
    subject = data["type"]
    send_email_function(send_email=sender, receiver_emails=emails,
                        password=password, subject=subject, content=body)
