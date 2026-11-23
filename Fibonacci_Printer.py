"""
Filename: n_fibonacci.py
Author: Raynor Matos Berry
Created: 11/17/2026
Instructor: Burgess
"""

def n_fibonacci():
    # Write your code here
    print("please enter a non negative whole number")
    n = int(input("Enter a number: "))
    x = 0
    y = 1
    for _ in range(n):
        print(x,end="")
        x, y = y, x + y,
        print(",",end="")


# You should not need to change any code below this point
def main():
    print("This program displays the standard Fibonacci sequence that is n elements long.")
    running = "y"
    while running == "y":
        n_fibonacci()
        running = input("\nPrint another sequence? (y/N)\n").lower()
    print("Thank you for using this standard Fibonacci sequence printer!")

if __name__ == "__main__":
    main()