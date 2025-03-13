from myapp.mymodule.funcs import multiply, divide


def multiply_by_two(x):
    return multiply(x, 2)


def divide_by_two(x):
    return divide(x, 2)


def square_area(side_length):
    return multiply(side_length, side_length)  # Area of a square = side^2