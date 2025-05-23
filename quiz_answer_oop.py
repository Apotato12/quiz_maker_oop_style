import os
import random

class FileCheck:
    def __init__(self, file_name="quiz.txt"):
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

def options(self,options):
    self.options = options
def correct_answer(self, correct_answer):
    self.correct_answer = correct_answer

class Quiz(FileCheck):
    def __init__(self, file_name="quiz.txt"):
        super().__init__(file_name)
        self.questions = []
    def read_questions(self):
        if not self.check_if_file_exists():
            return self.questions
        with open(self.file_name, "r") as file:
            lines = file.readlines()
        index = 0
        while index < len(lines):
            line = lines[index].strip()
            if line.startswith("Question: "):
                question_text = line[len("Question: "):]
                question = QuestionItems(question_text)
                options = self.options_reader(lines, index)
                question.set_options(options)
                correct_answer = self.correct_answer_reader(lines, index + len(options) + 1)
                question.set_correct_answer(correct_answer)
                self.questions.append(question)
                index += len(options) + 2
            else:
                index += 1
        return self.questions
    
    def options_reader(self, lines, start_index):
        options = {}
        for option_letter in ['a', 'b', 'c', 'd']:
            start_index += 1
            option_line = lines[start_index]
            start = f"Option {option_letter}: "
            if option_line.startswith(start):
                options[option_letter] = option_line[len(start):].strip()
            else:
                options[option_letter] = ""
        return options
    
    def correct_answer_reader(self, lines, index):
        correct_line = lines[index]
        if correct_line.startswith("Correct Answer:"):
            return correct_line[len("Correct Answer:"):].strip().lower()
    def display_questions(self):
        random.shuffle(self.questions)
        score = 0
        for question in self.questions:
            print(question.question_text)
            for option_letter, option_text in question.options.items():
                print(f"{option_letter}: {option_text}")
            user_answer = input("Please enter your answer: ").strip().lower()
            if user_answer == question.correct_answer:
                print("Correct")
                score += 1
            else:
                print(f"Wrong, the answer was {question.correct_answer}")
        print(f"Your final score is: {score}/{len(self.questions)}")