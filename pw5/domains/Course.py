class Course:
    def __init__(self, cid, name, ects):
        self.__id = cid
        self.__name = name
        self.__ects = ects
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def get_ects(self):
        return self.__ects

    def __str__(self):
        return f"{self.get_id()} - {self.get_name()} - {self.get_ects()} ECTS"

    def __repr__(self):
        return f"{self.get_id()}, {self.get_name()}, {self.get_ects()}\n"