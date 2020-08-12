import schedule

def do_print():
    print('hello world')

schedule.every(1).minutes.do(do_print)
schedule.every()

while 1:
    schedule.run_pending()  