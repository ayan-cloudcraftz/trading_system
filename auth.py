import schedule
import time
from lib.utils.reAuth import reAuthenticate
from tickle import tickle


def my_task():
    # reAuthenticate()
    tickle()


schedule.every(5
).minutes.do(my_task)

while True:
    schedule.run_pending()
    time.sleep(1)
