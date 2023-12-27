import email
import os
import smtplib
from email.message import EmailMessage
from passwords import password

def send_image_email(send_email, receiver_emails, password, subject, content_url):
    server = "smtp.gmail.com"
    msg = EmailMessage()
    msg["FROM"] = send_email
    msg["TO"] = receiver_emails
    msg["SUBJECT"] = subject

    for i in content_url:
        with open(i, "rb") as f:
            msg.add_attachment(f.read(), maintype="image", subtype="jpeg", filename=f.name.split("/")[-1])

    with smtplib.SMTP_SSL(server, 465) as server:
        server.login(send_email, password)
        server.send_message(msg)
        print("Email Sent {0}".format(" ".join(receiver_emails)))

if __name__ == '__main__':
    os.chdir("images")
    images = []
    for i in os.listdir():
        images.append(f"{os.getcwd()}/{i}")
    os.chdir("..")
    with open("email.list.py") as f:
        emails = [email.strip() for email in f.readlines()]
    send_image_email(send_email="khojiakbarme04@gmail.com", password=password,
                     receiver_emails=emails, subject="New Images", content_url=images)