import os

class Filename:
    def set_file_name(self, file_name="quiz.txt"):
        self.file_name = file_name
    
class FileMaker:
    def make_file(self, file_name):
        if not os.path.exists(file_name):
            open(file_name, 'w').close()
            print(f"File '{file_name}' has been created.")
        else:
            print(f"File '{file_name}' already exists.")

class QuestionParts:
    def ask_question(self):
        return input("Enter a question: ")
    
    def get_answers(self):
        answers = {}
        answers['a'] = input("Please enter option a: ")
        answers['b'] = input("Please enter option b: ")
        answers['c'] = input("Please enter option c: ")
        answers['d'] = input("Please enter option d: ")
        return answers
    
    def get_correct_answer(self):
         return input("Please enter the correct answer (a, b, c, or d): ")
    
class QuestionWriter:
    def __init__(self, file_name):
        self.file_name = file_name
    def save_question_to_file(self, question, answers, correct_answer):
        with open(self.file_name, "a") as file:
            file.write(f"Question: {question}\n")
            for option, answer in answers.items():
                file.write(f"Option {option}: {answer}\n")
            file.write(f"Correct Answer: {correct_answer}\n\n")
