# from email.message import EmailMessage
# import smtplib
#
# import requests
#
# from passwords import password
#
#
# sender = "khojiakbarme04@gmail.com"
# receiver = "imhojiakbar@gmail.com"
# server = "smtp.gmail.com"
# msg = EmailMessage()
# msg["From"] = sender
# msg["To"] = receiver
# msg["Subject"] = "CS GO"
# msg.set_content("I downloaded CS GO, can you join?")
#
# with smtplib.SMTP_SSL(server, 465) as server:
#     server.login(sender, password)
#     server.send_message(msg)
#     print("Email Sent to {}".format(receiver))
import requests


def send_request(url):
    data = requests.get(url).json()
    return data


if __name__ == '__main__':
    url = "https://wwwstatista.com/"
    print(send_request(url))
