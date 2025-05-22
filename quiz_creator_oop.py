import os

class Filename:
    def set_file_name(self, file_name="quiz.txt"):
        self.file_name = file_name
    
class FileMaker:
    def filename(self, filename_obj):
        self.file_name = filename_obj.file_name

def make_file(self):
        if not os.path.exists(self.file_name):
            open(self.file_name, 'w').close()
            print(f"File '{self.file_name}' has been created.")
        else:
            print(f"File '{self.file_name}' already exists.")

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