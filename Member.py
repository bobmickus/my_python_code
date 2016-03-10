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

    def add_coded_line(self, lines_of_code):
        self.lines_of_code.append(lines_of_code)
        num_lines_coded += 1
        get_coding_level(num_lines_coded)

    def get_coding_level(self, coding_level):
        if num_lines_coded <= 100:
            coding_level = "beginner"
        if num_lines_coded > 100 and num_lines_coded <= 1000:
            coding_level = 'novice'
        if num_lines_coded > 1000 and num <= 10000:
            coding_level = 'intermediate'
        else:
            coding_level = 'master'
