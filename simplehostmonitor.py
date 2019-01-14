import multiping
from datetime import datetime
import sys
import time


def curr_millis() -> int:
    return int(round(time.time() * 1000))


class SimpleHostMonitor:

    TIMEOUT = 5

    ERROR_HIGH_RTT = 'High RTT detected, host may be unresponsive.'
    ERROR_NO_RESPONSE = 'Host is unresponsive.'

    def __init__(self, host: str, max_rtt: int, max_retries: int, period: int):
        self.host: str = host
        self.max_rtt: int = max_rtt
        self.max_retries: int = max_retries
        self.period: int = period
        self.last_ping: int = curr_millis()

    def send_alert(self, message: str):
        print(message)
        pass

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
                    print(rtt)
                    if rtt > self.max_rtt:
                        self.send_alert(SimpleHostMonitor.ERROR_HIGH_RTT)

            self.last_ping = curr_millis()


if __name__ == '__main__':
    if len(sys.argv) < 5:
        print('Usage: python3.7 simplehostmonitor.py <HOST> <MAX_RTT> <MAX_RETRIES> <PERIOD>')
    else:
        monitor = SimpleHostMonitor(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        monitor.run()




