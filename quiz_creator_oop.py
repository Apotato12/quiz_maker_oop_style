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