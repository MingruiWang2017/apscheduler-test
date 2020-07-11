# encoding: utf-8

"""
@ author: wangmingrui
@ time: 2020/7/11 15:33
@ desc: 
"""
import threading
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


def get_time(id='my_job'):
    print("%-14s --> %s | thread: %s" % (id, datetime.now(), threading.current_thread()))

jobstores = {
    'default': MemoryJobStore()
}
executor = {
    'default': ThreadPoolExecutor(20),
    'process_pool': ProcessPoolExecutor(10)
}
job_defaults = {
    'coalesce': False,
    'max_instance': 3
}

scheduler = BlockingScheduler(jobstores=jobstores, executor=executor, job_defaults=job_defaults)
scheduler.add_job(get_time, args=['job_interval', ], id='job_interval', trigger='interval',
                  seconds=5, replace_existing=True) # replace_existing=True表示替换掉相同ID的job
scheduler.add_job(get_time, args=['job_cron', ], id='job_cron', trigger='cron',
                  hour='12-23', second='*/15', replace_existing=True)
scheduler.add_job(get_time, args=['job_once_now',], id='job_once_now')
scheduler.add_job(get_time, args=['job_date_once',], id='job_date_once', trigger='date',
                  run_date='2020-07-11 15:55:00')

if __name__ == '__main__':
    try:
        scheduler.start()
    except SystemExit:
        print('exit')
        exit()
