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