from lib2to3.pgen2.pgen import generate_grammar
import numpy as np


def default():
    print("Invalid example number")


def ex1():
    """
Given are 2 similar dimensional numpy arrays, 
how to get a numpy array output in which every element is an element-wise
sum of the 2 numpy arrays?"""
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b = np.array([[10, 11, 12],
                  [13, 14, 15]])

    c = a + b

    print(c)


# ex1()

def ex2():
    """Given a numpy array (matrix), how to get a numpy array
    output which is equal to the original matrix multiplied by a scalar?"""
    a = np.array([[1, 2, 3],
                  [4, 5, 6]])

    b = 2*a  # multiplying the numpy array a(matrix) by 2

    print(b)


def ex3():
    # Create an identity matrix of dimension 4-by-4
    i = np.eye(4)

    print(i)


# ex3()

def ex4():
    """1D arr to 3d arr"""
    a = np.array([x for x in range(27)])

    o = a.reshape((3, 3, 3))

    print(o)

# ex4()


def ex5():
    """Convert all the elements of a numpy array from float to integer datatype

"""
    a = np.array([[2.5, 3.8, 1.5],
                  [4.7, 2.9, 1.56]])

    o = a.astype('int')

    print(o)


# ex5()

def ex6():
    """Convert a binary numpy array (containing only 0s and 1s) to a boolean numpy array"""
    a = np.array([[1, 0, 0],
                  [1, 1, 1],
                  [0, 0, 0]])

    o = a.astype('bool')

    print(o)


def ex7(stack_dir="h"):
    """Stack 2 numpy arrays horizontally i.e., 2 arrays having the same 1st dimension (number of rows in 2D arrays)"""
    a1 = np.array([[1, 2, 3],
                   [4, 5, 6]])

    a2 = np.array([[7, 8, 9],
                   [10, 11, 12]])
    # use vstack to stack c=vertically
    if stack_dir == "h":
        # c = np.hstack((a1, a2))
        o = np.hstack((a1, a2))
        print(o)
    elif stack_dir == "v":
        o = np.vstack((a1, a2))
        print(o)
    else:
        print("Invalid direction, v/h")


switcher = {1: ex1, 2: ex2, 3: ex3, 4: ex4, 5: ex5, 6: ex6, 7: ex7}


def switch(ex_):
    switcher.get(ex_, default)()


switch(7)
