import os

class file_name():
    def file_name(self, file_name = "quiz.txt"):
     self.file_name = file_name
    
class file_maker():
   def make_file(self, file_name):
      if not os.path.exists(file_name):
         open(file_name, 'w').close
      else:
         print(f"file {file_name} already exists")