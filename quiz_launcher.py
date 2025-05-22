from quiz_creator_oop import Filename, FileMaker, QuestionParts, QuestionWriter, ContinueOrQuit

class QuizLauncher(Filename, FileMaker, QuestionParts, QuestionWriter):
    def __init__(self):
        Filename.__init__(self)
        FileMaker.__init__(self)
        self.set_file_name() 
        self.filename(self)  
        self.make_file()   


def run(self):
        while True:
            question = self.ask_question()
            answers = self.get_answers()
            correct_answer = self.get_correct_answer()
            self.save_question_to_file(question, answers, correct_answer)

            continue_or_quit = ContinueOrQuit()
            if continue_or_quit.another_question.lower() != "y":
                print("Exiting the program.")
                break

quiz_launcher = QuizLauncher()
quiz_launcher.run()