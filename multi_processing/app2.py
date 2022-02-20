import threading
import time

start = time.perf_counter()


def func(s=1):
    print(f"Sleep for {s} seconds")
    time.sleep(s)
    print("Done sleeping...")


threads = []

for _ in range(10):
    t = threading.Thread(target=func, args=[2.5])
    t.start()
    threads.append(t)

for th in threads:
    th.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")
