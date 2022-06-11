from EMailSender import EMailSender
from datetime import datetime, timedelta
import smtplib
from pytimecamp import Timecamp


class TimeCampMailer(EMailSender):
    options = {}
    message = ''
    timecamp = None

    def __init__(self, message: str, timecamp: Timecamp, options=None):
        self.message = message
        self.timecamp = timecamp
        self.options = options

    def update_message(self, message: str) -> None:
        self.message = message

    def get_message(self) -> str:
        return self.message

    def send(self) -> bool:
        with smtplib.SMTP_SSL(self.options['smtp_server'], self.options['port'],
                              context=self.options['context']) as server:
            server.login(self.options['sender_email'], self.options['password'])
            server.sendmail(self.options['sender_email'], self.options['receiver_email'], self.get_message())
            print("Your email was successfully sent!")
            return True

    def get_option(self, key: str):
        return self.options[key]

    def add_entries(self, num_of_days: int) -> None:
        me = list(self.timecamp.users)[0]
        set_from_date = datetime.today() - timedelta(days=num_of_days)

        for entry in self.timecamp.entries(from_date=set_from_date.date(), user_ids=[me.user_id]):
            start = datetime.strptime(entry.start_time, "%H:%M:%S")
            finish = datetime.strptime(entry.end_time, "%H:%M:%S")
            self.message += entry.date + " Start time: " + start.strftime(
                "%I:%M %p") + " End time: " + finish.strftime("%I:%M %p") + "\n "
