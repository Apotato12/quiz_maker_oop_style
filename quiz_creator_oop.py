import os

class Filename:
    def set_file_name(self, file_name="quiz.txt"):
        self.file_name = file_name
    
class FileMaker:
   def make_file(self, file_name):
      if not os.path.exists(file_name):
         open(file_name, 'w').close
      else:
         print(f"file {file_name} already exists")

def main_body():
   filename_obj = Filename()
   file_maker = FileMaker(filename_obj)
   file_maker.make_file()


main_body()