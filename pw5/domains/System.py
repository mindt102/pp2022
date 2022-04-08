import numpy as np
from domains.Utils import Utils
from domains.Student import Student
from domains.Course import Course

class System:
    def __init__(self):

        self.__files = {
            "data": "students.dat",
            "students": "students.txt",
            "courses": "courses.txt",
            "marks": "marks.txt"
        }
        Utils.extract(self.get_data_file())
        Utils.remove_file(self.get_data_file())

        self.__courses = self.load_courses()
        self.__num_courses = len(self.__courses)
        
        self.__students = self.load_students()
        self.__num_students = len(self.__students)

    def load_students(self):
        students = {}        
        marks = Utils.load_json(self.get_marks_file())
        for line in Utils.load(self.get_students_file()):
            sid, name, dob = map(str.strip, line.split(","))
            student = Student(sid, name, dob)
            if sid in marks:
                student.set_marks(marks[sid])
            else:
                student.set_marks({})
            self.calculate_gpa(student)
            students[sid] = student
        return students

    def load_courses(self):
        courses = {}
        for line in Utils.load(self.get_courses_file()):
            cid, name, ects = map(str.rstrip, line.split(","))
            courses[cid] = Course(cid, name, int(ects))
        return courses
    
    def get_num_students(self):
        return self.__num_students
    
    def get_num_courses(self):
        return self.__num_courses
    
    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def get_students_file(self):
        return self.__files["students"]

    def get_courses_file(self):
        return self.__files["courses"]

    def get_marks_file(self):
        return self.__files["marks"]

    def get_data_file(self):
        return self.__files["data"]
   
    def set_num_students(self):
        self.__num_students = Utils.input_number("students")
        print(f"==> There are {self.get_num_students()} student(s)")

    def set_num_courses(self):
        self.__num_courses = Utils.input_number("courses")    
        print(f"==> There are {self.get_num_courses()} course(s)")

    def set_students(self):
        print("Enter the students' info: ")
        self.__students = {}
        for i in range(self.get_num_students()):
            print(f"=> Student No. {i+1}")
            new_student = Student(
                input("\tEnter the student's id: "),
                input("\tEnter the student's name: "),
                input("\tEnter the student's dob: ")
            )
            self.__students[new_student.get_id()] = new_student
        Utils.save(self.get_students_file(), self.get_students().values())
        self.list_students()

    def set_courses(self):
        print("Enter the courses' info: ")
        self.__courses = {}
        for i in range(self.get_num_courses()):
            print(f"=> Course No. {i+1}")
            new_course = Course(
                input("\tEnter the course's id: "),
                input("\tEnter the course's name: "),
                int(input("\tEnter the number of credits: "))
            )
            self.__courses[new_course.get_id()] = new_course
        Utils.save(self.get_courses_file(), self.get_courses().values())
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

    def calculate_gpa(self, student:Student):
        courses = self.get_courses()
        marks = student.get_marks()
        if len(marks) == 0:
            student.set_gpa(0)
            return
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