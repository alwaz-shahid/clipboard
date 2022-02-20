import time

initial = time.time()

print(initial)
local_time = time.asctime(time.localtime(time.time()))

print(local_time)


def timer_f():
    print("Hey, I am a timer")
    print("wait for it...")
    time.sleep(2)
    input("Press enter to continue")


timer_f()
