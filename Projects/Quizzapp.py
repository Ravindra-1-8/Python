# Features of Quiz Masters:

# 1. Welcome Screen with App name and instructions.
# 2. Predefined set of multiple choice questions.
# 3. User answers with A, B, C, D
# 4. Correct and wrong answer checking.
# 5. Score calculations.
# 6. Display total score and percentage.
# 7. Performance feedback (Excellent / Good/ Practise score).
# 8. Option to play again (replay feature).

def quiz():
    print("Welcome to Quiz Masters!")
    print("\nInstructions: Answer the following multiple choice questions by typing the options given below.")
    
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Lisbon", "B. Paris", "C. London", "D. Amsterdam" ],
            "answer": "B"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A. Jupiter", "B. Pluto", "C. Earth", "D.Saturn"],
            "answer": "A"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A. H2O", "B. CO2", "C. NaCl", "D.CO2"],
            "answer": "A"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["A. William Shakespeare", "B. Charles Dickens", "C. Mark Twain", "D. Jane Austen"],
            "answer": "A"
        }
    ]
    
    
    
    score = 0
    
    for i, q in enumerate(questions, start = 1):
        print(f"\nQuestion {i} : {q['question']}")
        
        for option in q["options"]:
            print(option)
            
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}")
        
        
        
    total = len(questions)
    print(f"Quiz Completed!: {score}/{total}")
    
    percentage = (score/total) * 100
    print(f"\n Your Percentage: {percentage:.2f}%")
    
    if percentage >= 85:
        print("Excellent Performance!")
    elif percentage >= 65:
        print("Good Performance!")
    else:
        print("Keep Practising..!")
    
    retry = input("Do you want to try again (Y/N): ").lower()
    
    if retry =='y':
        quiz()
        
quiz() 