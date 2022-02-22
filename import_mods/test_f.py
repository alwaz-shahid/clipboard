def my_function(*args, **kwargs):
    print("Hello World \n" + str(args) + "\n" + str(kwargs))


# Defining our variable
name = "Nicholas"

# Defining a class


class Student:
    def __init__(self, name, course):
        self.course = course
        self.name = name

    def get_student_details(self):
        print("Your name is " + self.name + ".")
        print("You are studying " + self.course)
