from crontab import CronTab
cron = CronTab(user=True, tabfile='cyptoWatcherCron.tab', log='cryptoWatcherCron.log')
job = cron.new(command='python /Users/poteuse/PycharmProjects/cyptoWatcher/watcher.py >> /Users/poteuse/PycharmProjects/cyptoWatcher/cryptoWatcherCron.log')
job.minute.every(1)
cron.write()