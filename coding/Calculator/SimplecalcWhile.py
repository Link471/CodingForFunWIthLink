# John David
# 5/26/2023
# Purpose: To create a calculator that can be accessed from either the command-line or the Python Shell
# Version: 1.1

SN = "Second Number"
HELP = f"""This is JDCalc's help screen:
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
	- Input the second number you want to operate with on the line which should say "Second Number:

YOU CAN ACCESS THIS MENU AT ANY TIME BY TYPING 'HELP'
"""

print(HELP)

while True:
    FirstNumber = float(input("First Number: "))
    Operation = input("Operation: ")
    if Operation == "add" or Operation == "addition" or Operation == "+" or Operation == "more":
        print(FirstNumber + float(input(SN)))
    elif Operation == "subtract" or Operation == "minus" or Operation == "-" or Operation == "less":
        print(FirstNumber - float(input(SN)))
    elif Operation == "times" or Operation == "multiply" or Operation == "by" or Operation == "x" or Operation == "*":
        print(FirstNumber * float(input(SN)))
    elif Operation == "divide" or Operation == "divided" or Operation == "/":
        print(FirstNumber / float(input(SN)))
    elif Operation == "help":
        print(HELP)
    else:
        print("Unrecgonized option, try again.")
