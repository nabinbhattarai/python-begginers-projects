import time

def timer(t):
    while t:
        mins,secs = divmod(t, 60)
        counter = '{:02d}:{:02d}'.format(mins, secs)
        print(counter, end = "\r")
        time.sleep(1)
        t -=1

    print('Countdown is completed')

countdownTime = input("enter the countdown time in second: ")
timer(int(countdownTime))
