questions = {
    "What is the capital of India? ": "Delhi",
    "What is 5 + 3? ": "8",
    "Which language are you learning? ": "Python"
}

score = 0

for question, answer in questions.items():
    user_answer = input(question)

    if user_answer.lower() == answer.lower():
        print("Correct ")
        score += 1
    else:
        print("Wrong ")

print("Your final score:", score, "/", len(questions))
