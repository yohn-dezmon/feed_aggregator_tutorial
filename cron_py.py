from crontab import CronTab

empty_cron = CronTab()

job = cron.new(command='/usr/bin/echo')
