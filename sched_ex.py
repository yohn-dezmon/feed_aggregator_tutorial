import schedule
import time


def job():
    print("test test test")

def job2():
    print("test 2 test 2")

def job3():
    print("test 3 test 3")


schedule.every(10).seconds.do(job)
schedule.every(5).to(10).seconds.do(job2)
schedule.every().saturday.at("09:54").do(job3)


while True:
    schedule.run_pending()
    time.sleep(1)
