# quiz_game.py

questions = [
    {
        "question": "What does AI stand for?",
        "options": ["Artificial Intelligence", "All Information", "Artificial Insight", "Automated Interface"],
        "answer": "Artificial Intelligence"
    },
    {
        "question": "Which cryptocurrency uses smart contracts?",
        "options": ["Bitcoin", "Ethereum", "Litecoin", "Dogecoin"],
        "answer": "Ethereum"
    },
    {
        "question": "Who is the current president of the US?",
        "options": ["Joe Biden", "Donald Trump", "Barack Obama", "George Bush"],
        "answer": "Donald Trump"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for idx, opt in enumerate(q["options"], 1):
        print(f"{idx}. {opt}")
    choice = int(input("Enter the correct option number: "))
    if q["options"][choice - 1] == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {q['answer']}")

print(f"\nQuiz Over! Your Score: {score}/{len(questions)}")
