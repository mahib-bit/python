questions = ["What is the capital of Bangladesh?",
             "What is 2 + 2?",
             "What is the largest continent on Earth?",
             "What planet is known as the Red Planet?"
             ]

options = [["A. Dhaka", "B. Chittagong", "C. Khulna", "D. Rajshahi"],
           ["A. 3", "B. 4", "C. 5", "D. 6"],
           ["A. Africa", "B. Asia", "C. Europe", "D. Antarctica"],
           ["A. Mars", "B. Earth", "C. Jupiter", "D. Saturn"]
           ]

answers = ["A", "B", "C", "A"]
guesses = []
score = 0
question_num = 0

for question in questions:
    print ("-----------------------------")
    print (question)
    for option in options[question_num]:
        print(option)
    print()

    guess = input("Enter your answer (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
        print("The correct answer is:", answers[question_num])
    question_num += 1
print()
print("-----------------------------")
print(f"Final Results: {(score/len(questions)*100)}%")
print("-----------------------------")