from quiz_answer_oop import FileCheck, Quiz, QuestionItems

def main():
    quiz = Quiz()
    quiz.read_questions()
    if quiz.questions:
        quiz.display_questions()
    else:
        print("No questions to display.")



main()