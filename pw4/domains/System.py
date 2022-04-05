import imp
import numpy as np
from domains.Utils import Utils
from domains.Student import Student
from domains.Course import Course

class System:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = {}
        self.__courses = {}
    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def set_num_students(self):
        prev_num = self.get_num_students()
        self.__num_students = Utils.input_number("students")
        print(f"==> There are {self.get_num_students()} student(s)")
        if prev_num != self.get_num_students():
            self.set_students()

    def set_num_courses(self):
        prev_num = self.get_num_courses()
        self.__num_courses = Utils.input_number("courses")    
        print(f"==> There are {self.get_num_courses()} course(s)")
        if prev_num != self.get_num_courses():
            self.set_courses()

    def set_students(self):
        print("Enter the students' info: ")
        self.__students = {}
        for i in range(self.get_num_students()):
            print(f"=> Student No. {i+1}")
            new_student = Student()
            self.__students[new_student.get_id()] = new_student
        self.list_students()

    def set_courses(self):
        print("Enter the courses' info: ")
        self.__courses = {}
        for i in range(self.get_num_courses()):
            print(f"=> Course No. {i+1}")
            new_course = Course()
            self.__courses[new_course.get_id()] = new_course
        self.list_courses()

    # Display a list of students
    def list_students(self):
        if self.get_num_students() <= 0:
            print("There aren't any students yet")
            return
        print("==> Here is the student list: ")
        Utils.display(self.get_students())

    # Display a list of courses
    def list_courses(self):
        if self.get_num_courses() <= 0:
            print("There aren't any courses yet")
            return
        print("==> Here is the course list: ")
        Utils.display(self.get_courses())

    def calculate_gpa(self, std_id):
        student = self.get_students()[std_id]
        courses = self.get_courses()
        marks = student.get_marks()
        ects = []
        mark_lst = []
        for course in marks:
            ects.append(courses[course].get_ects())
            mark_lst.append(marks[course])

        result = round(np.dot(ects, mark_lst)/np.sum(ects),1)
        student.set_gpa(result)

    def sort_by_gpa(self):
        sorted_students = sorted(self.get_students().values(), reverse=True)
        print("Here is the list of student sorted by GPA")
        for i in range(self.get_num_students()):
            student = sorted_students[i]
            print(f"    {i+1}. {student.get_name():<20}{student.get_gpa()}")