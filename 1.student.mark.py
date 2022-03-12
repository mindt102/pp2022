def input_number(unit):
    return int(input(f"Enter the number of {unit} in this class: "));

def input_infos(item_type, infos):
    item = {}
    for info in infos:
        item[info] = input(f"\tEnter the {item_type}'s {info}: ")
    return item

def display(lst):
    for i, item in enumerate(lst):
        print(f"{1+i}. {item}")

def input_mark(student, course_id):
    if "marks" not in student:
        student["marks"] = {}
    student["marks"][course_id] = input("Enter the student's mark for this course: ")

def list_students(students):
    print("===> Here is the student list: ")
    for i, student in enumerate(students):
        print(f"{i+1}. {student['id']} - {student['name']} - {student['DoB']}")

def select(option_range, input_message="Choose an option: "):
    selection = input(input_message)
    if not selection.isnumeric():
        return -1
    selection = int(selection)
    if selection not in option_range:
        return -1
    return selection

def pause():
    input("Press Enter to continue...")

def main():
    courses = []
    students = []
    num_students = 0
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
    7. List students""")       
        selection = select(range(0, 8))
        if selection == 0:
            break
        elif selection == 1:
            num_students = input_number("students")
            print(f"===> There are {num_students} student(s) in this class")
        elif selection == 2:
            if num_students <= 0:
                print("Please input the number of students first")
                pause()
                continue
            for i in range(num_students):
                print(f"Student No. {i+1}")
                students.append(input_infos("student", ("id", "name", "DoB")))
            list_students(students)
        pause() 

    #num_courses = input_number("courses")
if __name__ == "__main__":
    main()
