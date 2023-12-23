class Student:
    def __init__(self,name,current_class,id):
        self.name = name
        self.current_class = current_class
        self.id = id
    def __repr__(self) -> str:
        return f'student whith name: {self.name},class:{self.current_class},id:{self.id}'

class Teacher:
    def __init__ (self,name,subject,id):
        self.name =name
        self.subject = subject
        self.id =id
    def __repr__(self) -> str:
        return f'Techer: {self.name},subject: {self.subject},id : {self.id}'

class School:
    def __init__ (self,name):
        self.name = name
        self.teacher = []
        self.student = []
    def add_teacher(self,name,subject):
        id = len(self.teacher)+101
        teacher = Teacher(name,subject,id)
        self.teacher.append(teacher)
    def enroll (self,name,fee):
        if fee < 6500:
            return 'not enough fee'
        else:
            id = len(self.student)+1
            student = Student(name,'C',id)
            self.student.append(student)
            return f'{name} is enrolled with id: {id},extra money{fee - 6500}'
    def __repr__(self) -> str:
        print('welcome to',self.name)
        print('-----OUR TEACHER -------')
        for teacher in self.teacher:
            print(teacher)
        print('-------OUT STUDENTS--------')
        for student in self.student:
            print(student)
        return 'ALL DONE FOR NOW'
# alia = student('alia torkari',9,1)
# print(alia)
phitron = School('phitron')
phitron.enroll('alia',5200)
phitron.enroll('rani',8000)
phitron.enroll('aishwaraya',7000)
phitron.enroll('vaijaan',900000)

phitron.add_teacher('tom cruise','algo')
phitron.add_teacher('decap','ds')
phitron.add_teacher('aj','database')

print(phitron)