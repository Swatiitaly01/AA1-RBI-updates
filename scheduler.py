from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
from datetime import datetime

def scheduled_job():
    print("Scheduled job executed at:", datetime.now(pytz.timezone('Asia/Kolkata')))

if __name__ == '__main__':
    scheduler = BlockingScheduler(timezone='Asia/Kolkata')
    scheduler.add_job(scheduled_job, 'cron', hour=6, minute=0)
    print("Scheduler started. It will execute daily at 6 AM IST.")
    scheduler.start()