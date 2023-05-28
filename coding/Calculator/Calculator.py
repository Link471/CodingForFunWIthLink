# John David
# 5/26/2023
# Purpose: To create a calculator that can be accessed from either the command-line or the Python Shell
# Version: 1.1

import CalculatorFuncs as CalcF
import sys


def calculator(operation, numbers):
    pass


def CalcHelp():
    print(f"""This is JDCalc's help screen:
Step 1: 
	- Input the first number you have on the line which should say "First Number:"

Step 2:
	- Write out which operation you would like to perform on the line which should say "Sekect Operation: "
	
    This calculator handles the following operations:
		- Addition        (Keywords: "add" "addition" "+" or "more"    )
		- Subtraction     (Keywords: "subtract" "minus" "-" or "less"  )
		- Multiplication  (Keywords: "times" multiply" "by" "*" or "x" )
		- Division        (Keywords: "divide" "divided" or "/"         )
        - Powered UP      (Keywords: "raised" "powered" "**" or "^"    )
                    
Step 3:
	- Input the second number you want to operate with on the line which should say "Second Number:"

Step 4:
	- If you would like to, you'll have the choice to clear the calculator leaving the value as 0
         
    """)


def __main__(argv):

    print(f"Welcome to JDCalculator! \nVersion: 0.0\n\n")
    CalcHelp()
    CalcF.InputCheck()


if __name__ == "__main__":
    __main__(sys.argv)
