import os
import smtplib
import ssl
from datetime import datetime, timedelta

from pytimecamp import Timecamp


def main():
    # Add our API-Key
    api_key = os.environ.get('TIMECAMP_API_KEY')
    tc = Timecamp(api_key)
    # SET THIS VARIABLE: Are you paid weekly, bi-weekly or monthly?
    PAY_TIME_FRAME = 'bi-weekly'.lower()
    me = list(tc.users)[0]

    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    sender_email = ""
    receiver_email = [""]
    smtp_server = 'smtp.gmail.com'
    message_subject = ""  # Add your subject line here.
    password = input("Type your password and press enter: ")
    message_text = ""

    num_of_days = 0
    if PAY_TIME_FRAME == 'bi-weekly':
        num_of_days = 14
    elif PAY_TIME_FRAME == 'weekly':
        num_of_days = 7
    else:
        num_of_days = 30

    set_from_date = datetime.today() - timedelta(days=num_of_days)  # Get the timeframe from today's date.
    for entry in tc.entries(from_date=set_from_date.date(), user_ids=[me.user_id]):
        start = datetime.strptime(entry.start_time, "%H:%M:%S")
        finish = datetime.strptime(entry.end_time, "%H:%M:%S")
        message_text += entry.date + " Start time: " + start.strftime("%I:%M %p") + " End time: " + finish.strftime("%I:%M %p") + "\n "

    message = "From: %s\r\n" % sender_email \
              + "To: %s\r\n" % ",".join(receiver_email) \
              + "Subject: %s\r\n" % message_subject \
              + "\r\n" \
              + message_text

    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Your email was successfully sent!")


if __name__ == '__main__':
    main()
