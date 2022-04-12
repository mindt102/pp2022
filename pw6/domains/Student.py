class Student:
    def __init__(self, sid, name, dob):
        self.__id = sid
        self.__name = name
        self.__dob = dob
        self.__marks = {}
        self.__gpa = 0

    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_dob(self):
        return self.__dob

    def get_marks(self):
        return self.__marks

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def set_marks(self, marks):
        self.__marks = marks
    
    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def __str__(self):
        result = f"{self.get_id()} - {self.get_name()} - {self.get_dob()}"
        marks = self.get_marks()
        if len(marks) > 0:
            result +=f"\n    {'Course':<10}: Mark   "
            for course_id, mark in marks.items():
                result += f"\n    {course_id:<10}: {mark}"
        if self.get_gpa() > 0:
            result += f"\n    {'GPA':<10}: {self.get_gpa()}"
        return result

    def __repr__(self):
        return f"{self.get_id()}, {self.get_name()}, {self.get_dob()}\n"

    def __lt__(self, other):
        return self.get_gpa() < other.get_gpa()