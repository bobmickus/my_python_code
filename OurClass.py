class OurClass():

    def __init__(self, name, location, size=0, members=None):
        self.name = name
        self.location = location
        self.size = size
        self.members = []

    def add_class_members(self, member):
        self.members.append(member)
        self.size += 1

    def check_if_at_capacity(self):
        if self.size >= 31:
           self.at_capacity = True
        else:
           self.at_capacity = False

    def get_num_questions_asked(self):
       num_questions_asked = 0
       for member in members:
           num_questions_asked += len(questions_asked)
       return num_questions_asked

    def get_num_lines_code(self):
       num_lines_coded = 0
       for member in members:
           num_lines_coded += num_lines_coded
       return num_lines_coded
