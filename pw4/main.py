from domains.System import *

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
