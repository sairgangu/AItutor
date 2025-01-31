import openai
import random



# openai.api_key = 

def generate_questions(subject, grade_level, num_questions):
    """
    Generate a list of questions for a specific subject and grade level.
    """
    questions = []
    for _ in range(num_questions):
        prompt = (
            f"Generate a {subject} question suitable for a grade {grade_level} student."
        )
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

def create_test(grade_level):
    """
    Create a test with 20 questions each from Math, Science, and ELA.
    """
    subjects = ["Math", "Science", "ELA"]
    test = {}
    for subject in subjects:
        test[subject] = generate_questions(subject, grade_level, 20)
    return test

def evaluate_answers(answers, correct_answers):
    """
    Evaluate the student's answers against the correct answers.
    """
    score = 0
    for student_answer, correct_answer in zip(answers, correct_answers):
        if student_answer.strip().lower() == correct_answer.strip().lower():
            score += 1
    return score

def adaptive_tutor(subject, grade_level, knowledge_gaps):
    """
    Adaptive tutor that teaches based on knowledge gaps.
    """
    print(f"Starting adaptive tutoring session for {subject}...")
    for topic in knowledge_gaps:
        print(f"Teaching topic: {topic}")
        while True:
            prompt = (
                f"Generate a {subject} question for a grade {grade_level} student focusing on {topic}."
            )
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a tutor providing adaptive learning."},
                    {"role": "user", "content": prompt},
                ],
            )
            question = response['choices'][0]['message']['content']
            print(f"Question: {question}")

            student_answer = input("Your Answer: ")
            correct_answer = "Correct answer placeholder"  # This would be dynamically generated
            if student_answer.strip().lower() == correct_answer.strip().lower():
                print("Correct! Moving to the next topic.")
                break
            else:
                print("That's not quite right. Let's try another question.")

if __name__ == "__main__":
    grade_level = int(input("Enter the student's grade level: "))
    print("Creating a personalized test...")
    test = create_test(grade_level)
    
    for subject, questions in test.items():
        print(f"\n{subject} Questions:")
        for i, question in enumerate(questions[:5]):
            print(f"{i + 1}. {question}")
    
    print("\nEvaluating the test...")
    student_answers = ["placeholder answer" for _ in range(60)]  # Simulated answers
    correct_answers = ["placeholder answer" for _ in range(60)]  # Placeholder correct answers
    score = evaluate_answers(student_answers, correct_answers)
    print(f"Student Score: {score}/60")
    
    knowledge_gaps = ["Fractions", "Photosynthesis"]  # Example topics
    adaptive_tutor("Math", grade_level, knowledge_gaps)
