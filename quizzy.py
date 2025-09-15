
def run_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")

    print("\nQuiz Completed!")
    print(f"Your final score: {score}/{len(questions)}")



quiz_questions = [
    {
        "question": "1. What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid", "D. Berlin"],
        "answer": "A"
    },
    {
        "question": "2. Which language is used for web apps?",
        "options": ["A. Python", "B. Java", "C. JavaScript", "D. All of the above"],
        "answer": "D"
    },
    {
        "question": "3. Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Elon Musk"],
        "answer": "B"
    }
]

