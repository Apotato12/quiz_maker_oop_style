import os
import random

class FileCheck:
    def set_file_name(self, file_name="quiz.txt"):
        self.file_name = file_name

    def check_if_file_exists(self):
        if os.path.exists(self.file_name):
            print("Quiz file exists")
            return True
        else:
            print("Quiz file does not exist. Please make one")
            return False
        
class QuestionItems:
    def __init__(self, question_text):
        self.question_text = question_text
        self.options = {}
        self.correct_answer = ""
    def set_options(self, options):
        self.options = options
    def set_correct_answer(self, correct_answer):
        self.correct_answer = correct_answer