"""
Filename: Average calculator.py
Author: Raynor Matos Berry
Created: 10/23/2026
Instructor: Burgess
"""
total=0
num=0
user = "y"
print("greetings user please enter a number")
while user == "y":



    number = int(input("enter a number: "))
    total = total+number
    print(f"sum: {total}")
    num = num+1
    print(f"current amount of numbers: {num}")
    print(f"average:{total/num}")
    user = input("would you like to enter another number (y/n): ")
