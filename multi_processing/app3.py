import threading
import time
import concurrent.futures

start = time.perf_counter()


def func(s=1):
    print(f"Sleep for {s} seconds")
    time.sleep(s)
    return "Done sleeping..."


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(func, 1)
    f2 = executor.submit(func, 1)
    print(f1.result())
    print(f2.result())


finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")
