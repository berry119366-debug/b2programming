"""
Filename: factorial_calculator.py
Author: Raynor Matos Berry
Created: 11/10/2026
Instructor: Burgess
"""

def factorial():
    # Write your code here
    print("please enter a non negative integer")
    number = int(input("Enter a number: "))


# You should not need to change any code below this point
def main():
    print("This program computes factorials and displays their intermediate calculations.")
    running = "y"
    while running == "y":
        factorial()
        running = input("Do another calculation? (y/N)\n").lower()
    print("Thank you for using this factorial calculator!")

if __name__ == "__main__":
    main()