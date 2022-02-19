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
