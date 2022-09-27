from email.message import EmailMessage
import smtplib
import ssl
import random
import requests

# make a random number for otp

otpCode = str(random.randint(1000, 2000))

email_sender = 'xxxxx@gmail.com'

email_password = 'xxxxxxxx'

email_receiver = input('Enter email:')

response = requests.get(
    "https://isitarealemail.com/api/email/validate",
    params={'email': email_receiver})
status = response.json()['status']
if status == "valid":
    print('Email valid')
    subject = 'Shatarko OTP'

    body = 'Shatarko otp is:' + otpCode

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as server:
        server.login(email_sender, email_password)
        server.sendmail(email_sender, email_receiver, em.as_string())
        print('OTP sent successfully')
elif status == "invalid":
    print('Email invalid')
else:
    print('Email is unknown.')
