import multiping
import smtplib
from email.mime.text import MIMEText
import sys
import time
from configparser import ConfigParser


def curr_millis() -> int:
    return int(round(time.time() * 1000))


class SimpleHostMonitor:

    TIMEOUT = 5

    ERROR_HIGH_RTT = 'High RTT detected, host may be unresponsive.'
    ERROR_NO_RESPONSE = 'Host is unresponsive.'

    def __init__(self, configuration_file_name: str):
        config = ConfigParser()
        config.read(configuration_file_name)

        self.host: str = config.get('monitoring_target', 'ip_address')
        self.max_rtt: int = int(config.get('monitoring_target', 'max_rtt'))
        self.max_retries: int = int(config.get('monitoring_target', 'max_allowed_failures'))
        self.period: int = int(config.get('monitoring_target', 'period'))

        self.mailjet_public_key: str = config.get('email', 'mailjet_public_key')
        self.mailjet_secret_key: str = config.get('email', 'mailjet_secret_key')
        self.sender_address: str = config.get('email', 'sender_address')
        self.send_email_to: str = config.get('email', 'send_email_to')
        self.last_ping: int = curr_millis()
        self.alarm_triggered: bool = False

    def send_email(self, subject: str, message: str):

        message = MIMEText(message)

        # me == the sender's email address
        # you == the recipient's email address
        message['Subject'] = subject
        message['From'] = self.sender_address
        message['To'] = self.send_email_to

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP('in-v3.mailjet.com')
        s.login(self.mailjet_public_key, self.mailjet_secret_key)
        s.sendmail(self.sender_address, [self.send_email_to], message.as_string())
        s.quit()

    def send_alert(self, message: str):
        if not self.alarm_triggered:
            self.alarm_triggered = True
            print(message)
            self.send_email(message, message)

    def run(self):
        while True:
            while (curr_millis() - self.last_ping) < self.period:
                pass

            mp = multiping.MultiPing([self.host])
            mp.send()
            responses, no_responses = mp.receive(SimpleHostMonitor.TIMEOUT)

            if no_responses:
                self.send_alert(SimpleHostMonitor.ERROR_NO_RESPONSE)
            else:
                for addr, rtt in responses.items():
                    rtt = rtt * 1000
                    if rtt > self.max_rtt:
                        self.send_alert(SimpleHostMonitor.ERROR_HIGH_RTT)
                    else:
                        self.alarm_triggered = False

            self.last_ping = curr_millis()


if __name__ == '__main__':
    monitor = SimpleHostMonitor('simplehostmonitor.conf')
    monitor.run()




