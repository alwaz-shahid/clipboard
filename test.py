import numpy as np
edit = False


def makeKwargs(**kwargs):
    print(kwargs)


while (edit):
    print("""
    1. Make a new kwargs
    2. Show all kwargs
    3. Exit
    """)
    choice = input("Enter choice: ")
    if choice == "1":
        print("Making a new kwargs")
        makeKwargs(**{"name": "John", "age": 23})
    elif choice == "2":
        print("Showing all kwargs")
        print(kwargs)
    elif choice == "3":
        print("Exiting")
        edit = False
    else:
        print("Unknown command, please try again")


# makeKwargs(a=1, b=2, c=3)


# Implement Python Switch Case Statement using Class

class PythonSwitch:

    def switch(self, dayOfWeek):
        default = "Incorrect day"
        return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

    def case_1(self):
        return "Monday"

    def case_2(self):
        return "Tuesday"

    def case_3(self):
        return "Wednesday"


s = PythonSwitch()

print(s.switch(1))
print(s.switch(3))
# print(s.switch(0))


def alternate_sols(sol=1):
    if sol == 1:
        list_of_numbers = [x for x in range(0, 101, 2)]
        o = np.array(list_of_numbers)
        print(o)
    elif sol == 2:
        o = np.arange(0, 101, 2)
        print(o)
