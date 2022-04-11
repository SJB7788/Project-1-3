import time

time1 = time.time()
print("hello")
time.sleep(1)
time2 = time.time()

totalTime = time2 - time1
if int(totalTime) == 1:
    print("Yo")