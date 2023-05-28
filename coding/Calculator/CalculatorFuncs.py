# John David
# 5/26/2023
# Purpose: To store the functions used in Calculator.py
# Version: 1.1

import math


def firstnumber(arg=0):
    print(arg, bool(arg), "chicken nugget")
    if arg:
        FirstNumber = arg
    else:
        FirstNumber = input("First Number: ")
    return float(FirstNumber)


def secondnumber():
    SecondNumber = input("Second Number: ")
    return float(SecondNumber)


def InputCheck():
    FirstNumber = firstnumber()
    operater = input("Select Operation: ")
    if operater == "add" or operater == "addition" or operater == "+" or operater == "more":
        JDAdd(FirstNumber)
    elif operater == "subtract" or operater == "minus" or operater == "-" or operater == "less":
        JDSubtract(FirstNumber)
    elif operater == "times" or operater == "multiply" or operater == "by" or operater == "*" or operater == 'x':
        JDMultiply(FirstNumber)
    elif operater == "divide" or operater == "divided" or operater == "/":
        JDDivide(FirstNumber)
    # This will be setting up the use of clearing the result from the running memmory.
    elif operater == "c" or operater == "CE":
        pass
    else:
        print("Not a recgonized value: Please Try again:")


def JDAdd(arg):
    result = arg + secondnumber()
    return print(result)


def JDSubtract(arg):
    result = arg - secondnumber()
    return print(result)


def JDMultiply(arg):
    result = arg * secondnumber()
    return print(result)


def JDDivide(arg):
    result = arg / secondnumber()
    return print(result)
