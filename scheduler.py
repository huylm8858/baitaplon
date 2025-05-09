import schedule
import time
import os

def job():
    os.system("python main.py")

schedule.every().day.at("06:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
