import sys

# Store at least 5 questions with answers 
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) London", "b) Paris", "c) Berlin", "d) Madrid"],
        "answer": "b"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["a) Ag", "b) Au", "c) Fe", "d) Gd"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["a) Venus", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "b"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["a) Central Processing Unit", "b) Computer Personal Unit", "c) Central Power Utility", "d) Core Program Utility"],
        "answer": "a"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"],
        "answer": "d"
    }
]

def run_quiz(questions: list) -> None:
    """
    Presents questions one by one, tracks the score, and shows the final result.
    """
    score = 0
    total_questions = len(questions)

    print("--- Starting the Multiple Choice Quiz ---")
    
    # Present questions one by one
    for i, q in enumerate(questions):
        print(f"\n--- Question {i + 1} of {total_questions} ---")
        print(q["question"])
        
        # Display options
        for option in q["options"]:
            print(option)

        # Accept user answers and normalize input
        while True:
            user_answer = input("Your answer (a, b, c, or d): ").strip().lower()
            if user_answer in ['a', 'b', 'c', 'd']:
                break
            print("Invalid input. Please enter only a, b, c, or d.")

        # Check answer and track score
        if user_answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            # Provide feedback and the correct answer
            print(f"❌ Incorrect. The correct answer was: {q['answer'].upper()}")

    # Show final result with percentage
    print("\n==============================")
    print("✨ QUIZ COMPLETE ✨")
    print(f"Your final score is: {score} out of {total_questions}")
    
    # Calculate and display percentage
    percentage = (score / total_questions) * 100 if total_questions > 0 else 0
    print(f"Percentage: {percentage:.2f}%")
    print("==============================")

# Test
run_quiz(questions)