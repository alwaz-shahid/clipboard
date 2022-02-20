import time


start = time.perf_counter()


def a_func():
    print("Hello, I am a function - 1")
    time.sleep(1)
    print("done sleeping")


a_func()
a_func()
a_func()
a_func()

finish = time.perf_counter()

print(f"Finished in {round(finish-start,2)} seconds")
