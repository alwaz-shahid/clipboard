
def nested_def(*args, **kwargs):
    print("Hello World \n" + str(args) + "\n" + str(kwargs))


# Defining our variable
name_n = "Nicholas"

# Defining a class


class Student:
    def __init__(self, name, course):
        self.course = course
        self.name = name

    def get_student_details(self):
        print("Your name is " + self.name + ".")
        print("You are studying " + self.course)
