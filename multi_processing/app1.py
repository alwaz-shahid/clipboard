import threading
import time

start = time.perf_counter()


def func():
    print("Sleep for 1 seconds")
    time.sleep(1)
    print("Done sleeping...")


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
'''
result when ran like this, t1 and t2 are not executed at the same time (copilot)


# t1.start()
# t2.start()

Sleep for 1 seconds
Sleep for 1 seconds
Finished in 0.0 seconds
Done sleeping...
Done sleeping...
'''
t1.start()
t2.start()

t1.join()
t2.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")
