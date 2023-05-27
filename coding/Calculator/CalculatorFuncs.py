# John David
# 5/26/2023
# Purpose: To store the functions used in Calculator.py
# Version: 0.0

import math


def firstnumber():
    FirstNumber = input("First Number: ")
    return float(FirstNumber)


def secondnumber():
    SecondNumber = input("Second Number: ")
    return float(SecondNumber)


def JDClear(arg):
    if arg:
        pass
    else:
        pass
    pass


def JDSelectOperater():
    FirstNumber = firstnumber()
    operater = input("Select Operation: ")
    if operater == "add" or operater == "addition" or operater == "+" or operater == "more":
        JDAdd(FirstNumber)
    elif operater == "subtract" or operater == "minus" or operater == "-" or operater == "less":
        JDAdd(FirstNumber)
    elif operater == "times" or operater == "multiply" or operater == "by" or operater == "*":
        JDAdd(FirstNumber)
    elif operater == "divide" or operater == "divided" or operater == "/":
        JDDivide(FirstNumber)


def JDAdd(arg):
    result = arg + secondnumber()
    return print(result)


def JDSubtract(arg):
    result = arg - secondnumber()
    return print(result)


def JDMultiply(arg):
    result = arg - secondnumber()
    return result


def JDDivide(arg):
    result = arg / secondnumber()
    return result
