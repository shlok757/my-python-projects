import time
score = 0
print("🎯 Welcome to the Ultimate Python Quiz Game! 🎯")
player_name = input("Enter your name: ")
print("\nHi", player_name + "! Let's test your knowledge.")
print("You will get 10 point for each correct answer.\n")
time.sleep(1)

questions = [
    {
        "question": "1. What is the output of print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 5"],
        "answer": "B"
    },
    {
        "question": "2. Which of the following is a Python data type?",
        "options": ["A. integer", "B. string", "C. boolean", "D. all of these"],
        "answer": "D"
    },
    {
        "question": "3. What keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "4. Which of these is used to take input from the user?",
        "options": ["A. input()", "B. scanf()", "C. cin>>", "D. get()"],
        "answer": "A"
    },
    {
        "question": "5. What is the correct file extension for Python files?",
        "options": ["A. .pyth", "B. .pt", "C. .py", "D. .python"],
        "answer": "C"
    }
]



for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    while True:
        ans = input("Enter your answer (A/B/C/D): ").upper()
        if ans in ["A", "B", "C", "D"]:
            break
        else:
            print("⚠️ Please enter a valid option (A, B, C, or D).")

    if ans == q["answer"]:
        print("✅ Correct!")
        score += 10
    else:
        print("❌ Wrong! The correct answer was:", q["answer"])
    time.sleep(0.8)

print("\n🎉 Quiz Completed! 🎉")
print(player_name + ", your final score is:", score, "out of", len(questions))

if score == len(questions):
    print("🏆 Excellent! You got a perfect score!")
elif score >= 3:
    print("👏 Great job! You did really well!")
else:
    print("💡 Keep practicing! You'll get better next time.")

print("\nThanks for playing, " + player_name + "! 👋")