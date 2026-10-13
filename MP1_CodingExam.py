"""
Author: Raynor Matos Berry
MP1_Exam
"""
print("greetings user, please insert your current test score")
score = int(input("Enter your current test score: "))
if score >= 90:
    print("Awesome job!")
    print("grade:A")
elif score >= 80:
    print("Awesome job!")
    print("grade:B")
elif score >= 70:
    print("Keep practicing!")
    print("grade:C")
elif score >= 60:
    print("Keep practicing!")
    print("grade:D")
elif score < 60:
    print("Keep practicing!")
    print("grade:F")
