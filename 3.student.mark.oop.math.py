import math
import numpy as np

class Student:
    def __init__(self):
        self.__id = input("\tEnter the student's id: ")
        self.__name = input("\tEnter the student's name: ")
        self.__dob = input("\tEnter the student's dob: ")
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

    def __lt__(self, other):
        return self.get_gpa() < other.get_gpa()

class Course:
    def __init__(self):
        self.__id = input("\tEnter the course's id: ")
        self.__name = input("\tEnter the course's name: ")
        self.__ects = int(input("\tEnter the number of credits"))
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_ects(self):
        return self.__ects

    def __str__(self):
        return f"{self.get_id()} - {self.get_name()} - {self.get_ects()} ECTS"

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
class Utils:
    # Ask the user to input a number
    def input_number(unit):
        return int(input(f"Enter the number of {unit} in this class: "));

    # Display a list of items
    def display(dct):
        for i, item in enumerate(dct.values()):
            print(str(i+1) + ".", end=" ")
            print(item)

    # Ask the user to enter an integer to select an option
    def select(option_range, input_message="Choose an option: "):
        selection = input(input_message)
        if not selection.isnumeric():
            return -1
        selection = int(selection)
        if selection not in option_range:
            return -1
        return selection

    # Pause the program
    def pause():
        input("Press Enter to continue...")

# Main function
def main():
    system = System()
    while(True):
        print("""
===================================================
Here are the functions of this application
    0. Exit
    1. Input number of students
    2. Input students information (id, name, DoB)
    3. Input number of courses
    4. Input course information (id, name)
    5. Input marks for student in a course
    6. List courses
    7. List students
    8. Sort the student list by GPA descending""")       
        selection = Utils.select(range(0, 9))
        if selection == 0:
            break
        elif selection == 1:
            system.set_num_students()
        elif selection == 2:
            if system.get_num_students() <= 0:
                print("Please input the number of students first")
                Utils.pause()
                continue
            system.set_students()
        elif selection == 3:
            system.set_num_courses()
        elif selection == 4:
            if system.get_num_courses() <= 0:
                print("Please input the number of courses first")
                Utils.pause()
                continue
            system.set_courses()
        elif selection == 5:
            system.list_courses()
            if system.get_num_courses() > 0:
                selected_course = input("Select a course: ") 
                if selected_course not in system.get_courses():
                        print("Invalid input")
                else:
                    for std_id, student in system.get_students().items():
                        print(f"Student ID: {std_id} - {student.get_name()}. ",end="")
                        student.add_mark(selected_course, round(float(input("Enter the student's mark for this course: ")), 1)) 
                        system.calculate_gpa(std_id)
        elif selection == 6:
            system.list_courses()
        elif selection == 7:
            system.list_students()
        elif selection == 8:
            system.sort_by_gpa()
        else:
            print("Invalid input. Please try again!")
        Utils.pause() 

if __name__ == "__main__":
    main()
