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
