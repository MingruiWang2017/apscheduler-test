# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2020/7/11 11:53
@ desc: 
"""

import threading
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def get_time():
    print("Time: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def get_time2():
    print("-----Time: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "-----")


def timer1():
    scheduler1 = BlockingScheduler()
    scheduler1.add_job(get_time, 'interval', seconds=5)  # 最后的关键字参数是传递给interval trigger 的构造参数

    scheduler2 = BlockingScheduler()
    scheduler2.add_job(get_time2, 'cron', minute="*/1")

    thread1 = threading.Thread(target=scheduler1.start)
    thread2 = threading.Thread(target=scheduler2.start)

    try:
        thread1.start()
        thread2.start()
    except (KeyboardInterrupt, SystemExit):
        print("exit timer1")


def timer2():
    scheduler = BlockingScheduler()
    scheduler.add_job(get_time, 'interval', seconds=5)
    scheduler.add_job(get_time2, 'cron', minute="*/1")

    try:
        scheduler.start()
    except KeyboardInterrupt:
        print("exit timer2")


if __name__ == '__main__':
    # timer1()
    timer2()
