take_args = True


def acpt_args(*args):
    for item in args:
        print(item)


a = [1, 2, 3, 4, 5]

acpt_args(a)
print("Press Y to enter value, N to get results. type exit to exit")
arr = []
dec = input("Enter choice: Y/n")
if len(arr) == 0 and dec == "n":
    print("Exiting, empty array")
elif dec == "y":
    while acpt_args:
        val = input("Enter value: ")
        arr.append(val)
        if val == "exit":
            acpt_args(arr)
            break
    # acpt_args(arr)
else:
    print("Exiting, invalid input")

# user_input = input("Enter a something: ")
# arr.append(user_input)
