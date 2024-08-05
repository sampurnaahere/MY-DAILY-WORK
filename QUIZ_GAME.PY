import random

questions = [
    {"question": "What is the capital of France?", "choices": ["A) Paris", "B) London", "C) Rome", "D) Berlin"], "answer": "A"},
    {"question": "What is 2 + 2?", "choices": ["A) 3", "B) 4", "C) 5", "D) 6"], "answer": "B"},
    {"question": "What is the chemical symbol for gold?", "choices": ["A) Au", "B) Ag", "C) Fe", "D) Hg"], "answer": "A"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "choices": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"], "answer": "A"},
    {"question": "What is the largest planet in our solar system?", "choices": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"], "answer": "C"}
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions.")
    print("Select the correct answer by choosing the corresponding letter.")
    print("Let's see how many you can get right!")
    print()

def ask_question(question):
    print(question["question"])
    for choice in question["choices"]:
        print(choice)
    user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
    return user_answer

def evaluate_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    return False

def display_feedback(is_correct, correct_answer):
    if is_correct:
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer was: {correct_answer}")

def display_final_results(score, total_questions):
    print()
    print(f"Your final score is {score} out of {total_questions}.")
    if score == total_questions:
        print("Excellent job! You got everything right!")
    elif score >= total_questions / 2:
        print("Good job! You got more than half right.")
    else:
        print("Better luck next time!")

def play_quiz():
    score = 0
    total_questions = len(questions)
    
    display_welcome_message()

    for question in questions:
        user_answer = ask_question(question)
        is_correct = evaluate_answer(user_answer, question["answer"])
        display_feedback(is_correct, question["answer"])
        if is_correct:
            score += 1
        print()

    display_final_results(score, total_questions)

def main():
    while True:
        play_quiz()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
           print("thank you for playing today")
           break

if __name__ == "__main__":
    main()


