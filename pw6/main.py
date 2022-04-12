from domains.System import *

# Main function
def main():
    system = System()
    while(True):
        print("""
===================================================
Here are the functions of this application
    0. Exit
    1. Update students
    2. Update courses
    3. Update students' marks in a course
    4. List courses
    5. List students
    6. Sort the student list by GPA descending""")       
        selection = Utils.select(range(0, 7))
        if selection == 0:
            files = (system.get_students_file(), system.get_courses_file())
            Utils.zipfiles(system.get_data_file(), files)
            # for file in files:
            #     Utils.remove_file(file)
            break
        elif selection == 1:
            system.set_num_students()
            system.set_students()
            # Utils.save_json(system.get_marks_file(), {})
        elif selection == 2:
            for student in system.get_students().values():
                student.set_marks({})
                student.set_gpa({0})
            Utils.save(system.get_students_file(), system.get_students())
            # Utils.save_json(system.get_marks_file(), {})
            system.set_num_courses()
            system.set_courses()
        elif selection == 3:
            system.list_courses()
            if system.get_num_courses() > 0:
                cid = input("Select a course: ") 
                if cid not in system.get_courses():
                        print("Invalid input")
                else:
                    # marks = Utils.load_json(system.get_marks_file())
                    for sid, student in system.get_students().items():
                        print(f"Student ID: {sid} - {student.get_name()}. ",end="")
                        mark = round(float(input("Enter the student's mark for this course: ")), 1)
                        student.add_mark(cid, mark)
                        system.calculate_gpa(student)
                    #     if sid not in marks:
                    #         marks[sid] = {}
                    #     marks[sid][cid] = mark
                    # Utils.save_json(system.get_marks_file(), marks)
                    Utils.save_pickle(system.get_students_file(), system.get_students())
                    
        elif selection == 4:
            system.list_courses()
        elif selection == 5:
            system.list_students()
        elif selection == 6:
            system.sort_by_gpa()
        else:
            print("Invalid input. Please try again!")
        Utils.pause() 

if __name__ == "__main__":
    main()
