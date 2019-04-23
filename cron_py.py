# from crontab import CronTab
# # https://stackabuse.com/scheduling-jobs-with-python-crontab/
#
# # accessing cron...
# cron = CronTab(user=True)
# # set the task to be run
# job = cron.new(command='python /Users/HomeFolder/taskqueue_tut/run.py')
# # set frequency that it should be run!
# job.minute.every(1)
# # this is key, this adds our job to cron! :D
# cron.write()
#
#
# # ok result: this is putting * * * * * /Users/HomeFolder/taskqueue_tut/run.py into the
# # crontab... but it is still not working! Like I cannot open the website... IDK if it is affecting
# # the database.
#
#
# # ah apparently I have to make run.py executable! :D
# # I do this with chmod +x run.py
