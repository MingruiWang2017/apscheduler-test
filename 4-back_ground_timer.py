# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2020/7/13 17:08
@ desc: 
"""
import datetime
import time
import os
from apscheduler.schedulers.background import BackgroundScheduler


def printTime(f):
    now_time = "Now: %s" % datetime.datetime.now()
    print(now_time)
    f.write(now_time + "\n")
    f.flush()


if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    with open("test.txt", 'a+') as f:
        scheduler.add_job(printTime, args=[f, ], trigger='interval', seconds=3)
        scheduler.start()
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

        try:
            # This is here to simulate application activity (which keeps the main thread alive).
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            # Not strictly necessary if daemonic mode is enabled but should be done if possible
            scheduler.shutdown()
