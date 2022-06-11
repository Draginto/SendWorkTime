import os
import ssl
from src.enums.PayPeriod import PayPeriod
from pytimecamp import Timecamp
from src.TimeCampMailer import TimeCampMailer
import time
from smtpapi import SMTPAPIHeader


def main():
    # Add our API-Key
    timecamp_api_key = ""
    sendgrid_api_key = ""
    tc = Timecamp(timecamp_api_key)

    # SET THIS VARIABLE: Are you paid weekly, bi-weekly or monthly?
    PAY_TIME_FRAME = input("Are you paid weekly, bi-weekly or monthly?").upper().strip()

    # selected_sender = input('Please enter your email:').strip()
    # password = input('Please enter your password:').strip()
    selected_receiver = input('Please enter the email you are sending to: ').strip()

    mailing_options = {
        'context': ssl.create_default_context(),
        'port': 465,
        'sender_email': "apiKey",
        'receiver_email': selected_receiver,
        'smtp_server': 'smtp.sendgrid.net',
        'message_subject': '',
        'password':  sendgrid_api_key,
        'message_text': ""
    }

    if PAY_TIME_FRAME == PayPeriod.BI_WEEKLY:
        num_of_days = 14
    elif PAY_TIME_FRAME == PayPeriod.WEEKLY:
        num_of_days = 7
    else:
        num_of_days = 30

    message = "From: %s\r\n" % mailing_options['sender_email'] \
              + "To: %s\r\n" % ",".join(mailing_options['receiver_email']) \
              + "Subject: %s\r\n" % mailing_options['message_subject'] \
              + "\r\n" \
              + mailing_options['message_text']

    mailer = TimeCampMailer(message, tc, mailing_options)
    mailer.add_entries(num_of_days)
    mailer.send()


if __name__ == '__main__':
    main()
