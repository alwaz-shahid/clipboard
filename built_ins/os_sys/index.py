import os

# get user info


def f_calls():
    print("Hello, I am a function")
    d = dir(os)
    # print(d)
    # os.mkdir(f_name) male folder
    # os.mkdirs(f_name/sub_f_name) make folders
    cwd = os.getcwd()
    print("current working directory is: ", cwd)


f_calls()
