# description 
"""
Desc: A simple calculator with python
Author: Oscar Rodriguez


"""

# imports 


# global variables

# function (declarations)
def print_menu():
    print("*" * 20)
    print(" Super Pycalc 5000")
    print("*" * 20)

    print("[1] Sum two numbers")
    print("[2] Subtract two numbers")
    print("[3] multiply two numbers")
    print("[4] Divide two numbers")
    print("[5] Guess my age")

    print("[x] Quit")
"""

"""

# instructions 
opt = ""
while(opt != "x"):
    print_menu()

    opt = input("Please select an option:")
    if opt  == "x":
        break

    if opt != "5":
     num1= float(input("Please provide number 1:"))
     num2 = float(input("Please provide number 2:"))
    else:
        year = int(input("please Provide your birth year:"))

    if opt == "1":
        print(f"the Result is: + {num1 + num2}")

    elif opt == "2":
        print(f"the Result is: + {num1 - num2}")

    elif opt == "3": 
        print(f"the Result is: + {num1 * num2}" )

    elif opt == "4":
        if (num2 == 0):
            print("Error: Unknow magic spotted")
        else:
            print(f"the result is {num1/num2}")

    elif opt == "5":
         print(f"You are {2021-year} years old, probably.")



    input("Please press Enter to continute...") 
        

print("Good bye!")