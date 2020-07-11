# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2020/7/11 16:04
@ desc: 
"""
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
import logging
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s [line: %(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S.x',
                    filename='log1.txt',
                    filemode='a')


def aps_test(x):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)


def aps_test_error(x):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), x)
    print(100 / x)  # 故意抛出异常


def my_listener(event):
    if event.exception:
        print("任务出错！！！")
    else:
        print('任务正常……')


scheduler = BlockingScheduler()
scheduler.add_job(func=aps_test, args=("正常任务",), trigger='cron',
                  second='*/5', id="cron_task")
scheduler.add_job(func=aps_test_error, args=("一次性任务，会出错",),
                  next_run_time=datetime.now() + timedelta(seconds=7), id='date_task')

# 添加事件监听器
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# 设置日志，报错信息可在logfile中查看
scheduler._logger = logging

scheduler.start()
