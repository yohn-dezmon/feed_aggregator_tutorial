class Student(object):

#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
# scott = Student('Scott', 'Robinson')

    @classmethod
    def from_string(cls):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student

    scott = Student.from_string('Scott Robinson')
