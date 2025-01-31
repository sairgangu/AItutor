import openai

def get_api_key():
    """Prompt the user to enter their OpenAI API key."""
    return input("Enter your OpenAI API key: ")

def generate_questions(subject, grade_level, num_questions):
    """Generate a list of diagnostic test questions for a specific subject and grade level."""
    openai.api_key = get_api_key()
    questions = []
    for _ in range(num_questions):
        prompt = f"Generate a {subject} question suitable for a grade {grade_level} student."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a tutor generating questions."},
                {"role": "user", "content": prompt},
            ],
        )
        question = response['choices'][0]['message']['content']
        questions.append(question)
    return questions

def administer_test(grade_level):
    """Give the student 20 questions per subject without assistance."""
    subjects = ["Math", "Science", "English"]
    test_results = {}
    
    for subject in subjects:
        print(f"\n{subject} Diagnostic Test")
        test_results[subject] = []
        questions = generate_questions(subject, grade_level, 20)
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
            answer = input("Your Answer: ")
            test_results[subject].append((question, answer))
    
    return test_results

def evaluate_test(test_results):
    """Analyze test results to identify knowledge gaps."""
    knowledge_gaps = {}
    for subject, responses in test_results.items():
        incorrect_answers = []
        for question, answer in responses:
            correct_answer = "Correct answer placeholder"  # Replace with real answer-checking logic
            if answer.strip().lower() != correct_answer.strip().lower():
                incorrect_answers.append(question)
        if incorrect_answers:
            knowledge_gaps[subject] = incorrect_answers
    return knowledge_gaps

def teach_lesson(subject, knowledge_gaps):
    """Provide a lesson based on identified knowledge gaps."""
    print(f"\nTeaching {subject}...")
    for topic in knowledge_gaps:
        print(f"\nLesson on: {topic}")
        explanation = f"Explain {topic} to a {subject} student."
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a tutor explaining concepts."},
                {"role": "user", "content": explanation},
            ],
        )
        print(response['choices'][0]['message']['content'])
        input("Type 'r' when ready to move on: ")
        for _ in range(3):
            question_prompt = f"Generate a practice question about {topic}."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a tutor generating practice questions."},
                    {"role": "user", "content": question_prompt},
                ],
            )
            question = response['choices'][0]['message']['content']
            print(f"Question: {question}")
            answer = input("Your Answer: ")

def main():
    """Run the AI tutor."""
    grade_level = int(input("Enter your grade level: "))
    print("\nStarting Diagnostic Test...")
    test_results = administer_test(grade_level)
    knowledge_gaps = evaluate_test(test_results)
    for subject, gaps in knowledge_gaps.items():
        teach_lesson(subject, gaps)

if __name__ == "__main__":
    main()
