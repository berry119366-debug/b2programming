"""
Author: Raynor Matos Berry
MP1_Exam
"""
f=int(input("fahrenheit:"))
c=((f-32) * 5/9)
print(c)
if c > 35:
    print("Heat Warning!")
elif c < 0:
    print("Freezing Alert!")
else:
    print("Normal temperature")




