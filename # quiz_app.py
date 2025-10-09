# quiz_app.py

# Define the quiz questions
quiz = [
    {
        "question": "Which festival is called the festival of lights?",
        "options": ["Diwali", "Holi", "Eid", "Baisakhi", "Onam"],
        "answer": "Diwali"
    },
    {
        "question": "Which festival is known for colors?",
        "options": ["Eid", "Diwali", "Holi", "Raksha Bandhan", "Lohri"],
        "answer": "Holi"
    }
]

score = 0

# Loop through each question
for i, q in enumerate(quiz):
    print(f"\nQuestion {i+1}: {q['question']}")
    
    for index, option in enumerate(q['options']):
        print(f"{index + 1}. {option}")
    
    try:
        choice = int(input("Enter the number of your choice: "))
        if q['options'][choice - 1] == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is: {q['answer']}")
    except (ValueError, IndexError):
        print("⚠️ Invalid input. Please enter a number between 1 and 5.")

# Show final score
print(f"\n🎉 You got {score} out of {len(quiz)} correct!")
