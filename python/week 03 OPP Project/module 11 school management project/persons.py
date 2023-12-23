import random
from school import School
class Person:
    def __init__(self,name) -> None:
        self.name = name
class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
        # self.subject = subject
    def teach(self):
        pass
    def __repr__(self) -> str:
        return f'{self.name} '
    
    def evaluate_exam(self):
        marks = random.randint(0,100)
        return marks
        
class Student(Person):

    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.__id = None
        self.classroom = classroom
        self.marks = {}
        self.subject_gread = {}
        self.grade = None
    def calculate_final_grade(self):
        sum = 0
        for grade in self.subject_gread.values():
            point = School.grade_to_value(grade)
            sum += point
            print(self.name, grade, point)
        points_avg = sum/len(self.subject_gread)
        self.grade = School.value_to_grade(points_avg)
        print(f'{self.name} final grade: {self.grade} with pints avg{points_avg}')
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id = value