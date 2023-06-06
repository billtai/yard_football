from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler(daemon=True,timezone="Asia/Ho_Chi_Minh")
scheduler = APScheduler(scheduler=sched)