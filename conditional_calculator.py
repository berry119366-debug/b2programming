"""
Filename: conditional_calculator.py
Author: Raynor Matos Berry
Created 9/10/2026
Instructor: Burgess
"""
print("greetings user this calculator is used for adding, subtracting, multiplication, division")
n1=int(input("num:"))
op=input("operation:")
n2=int(input("num:"))
print(f"{n1} {op} {n2}")
if op=="+":
    print("answer:",(n1+n2))
elif op=="-":
    print("answer:",(n1-n2))
elif op=="/":
    print("answer:",(n1/n2))
elif op=="*":
    print("answer:",(n1*n2))
else:
    print("invalid operation")
print("thank you for using this calculator program")