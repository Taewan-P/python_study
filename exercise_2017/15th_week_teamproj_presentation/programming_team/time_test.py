def stopWatch():
    import time
    a = 0
    hours = 0
    while a < 1:
        for minutes in range(0, 60):
            for seconds in range(0, 60):
                time.sleep(1)
                print(hours,":", minutes,":", seconds)
    hours = hours + 1

stopWatch()