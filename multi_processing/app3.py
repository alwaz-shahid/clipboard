import threading
import time
import concurrent.futures

start = time.perf_counter()


def func(s=1):
    print(f"Sleep for {s} seconds")
    time.sleep(s)
    return "Done sleeping..."


with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5.3, 2.5, 4.5]
    # list comprehension
    # results = [executor.submit(func, sec) for sec in secs]
    # results = [executor.submit(func, 1) for _ in range(10)]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    # f1 = executor.submit(func, 1)
    # f2 = executor.submit(func, 1)
    # print(f1.result())
    # print(f2.result())
    results = executor.map(func, secs)
    for result in results:
        print(result)


finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")
