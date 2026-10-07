"""
Filename:trivia_game.py
Author: Raynor Matos Berry
Created: 9/28/2026
Instructor: Burgess
"""
print("Welcome to Trivia Game, This is a short quiz that will be put into the gradebook once finished")
score = 0
correct_answers = 0
q1=input(f"What is the largest country in the world?")
if q1 == "russia":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if score > 0:
        score -= 10
        correct_answers -= 1
q2=input(f"what is the capital of the united states?")
if q2 == " washington DC":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if score > 0:
        score -= 10
q3=input(f"what is the most commonly spoken language in the world?")
if q3 == "english":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
q4=input(f"what is 12*2?")
if q4 == "24":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
q5=input(f"what is 20/4?")
if q5 == "5":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
q6=input(f"what is 2+2?")
if q6 == "4":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
q7=input(f"what is the chemical formula for water?")
if q7 == "H2O":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
q8=input(f"what is the atomic number for hydrogen?")
if q8 == "1":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
q9=input(f"what is the first family in the periodic table?")
if q9 == "Akali metals":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
q10=input(f"what is the most used coding language?")
if q10 == "Java":
    score += 10
    correct_answers += 1
    print("correct")
else:
    print("incorrect")
    if correct_answers > 0:
        score -= 10
print("final score:", score)
print("correct answers:", correct_answers)
print("incorrect answers:", incorrect_answers)
print("Thank you for completing this trivia quiz")
