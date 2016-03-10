class Member():

    def __init__(self, name, hair_color, birthdate):
        self.name = name
        self.hair_color = hair_color
        self.birthdate = birthdate
        self.questions_asked = []
        self.lines_of_code = []
        self.num_lines_coded = 0
        self.coding_level = 'beginner'

    def add_question_asked(self, question):
        self.questions_asked.append(question)

    def get_coding_level(self,num_lines_coded):
      if num_lines_coded <= 100:
        coding_level = "beginner"
      if num_lines_coded > 100 and num_lines_coded <= 1000:
        coding_level = 'novice'
      if num_lines_coded > 1000 and num_lines_coded <= 10000:
        coding_level = 'intermediate'
      else:
        coding_level = 'master'
      return coding_level

    def add_coded_line(self, line_of_code):
        self.lines_of_code.append(line_of_code)
        self.num_lines_coded += 1
        self.coding_level = get_coding_level(self.num_lines_coded)
