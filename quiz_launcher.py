from quiz_creator_oop import Filename, FileMaker, QuestionParts, QuestionWriter

class QuizLauncher(Filename, FileMaker, QuestionParts, QuestionWriter):
 def __init__(self):
        Filename.__init__(self)
        self.set_file_name()
        self.make_file(self.file_name)
        QuestionWriter.__init__(self, self.file_name)   

 def run(self):
        while True:
            question = self.ask_question()
            answers = self.get_answers()
            correct_answer = self.get_correct_answer()
            self.save_question_to_file(question, answers, correct_answer)
            

quiz_launcher = QuizLauncher()
quiz_launcher.run()
