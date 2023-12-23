class student:
    print("\n\t\t--------Walcame to our school-------------\n ")
    print("\n\t our school name is : python lurning instation (PLI)\n\t" )
    def __init__(self,name,subject,marks) -> None:
        self.name = name
        self.subject = subject
        self.marks = marks
        self.grade = []
        self.grade_chack()
    def grade_chack(self):
        if self.marks >= 80:
            self.grade.append('A')
        elif self.marks >= 60:
            self.grade.append('B')
        else:
            self.grade.append('F')
    def student_detels(self):
        print(f"student name : {self.name}\n student subject : {self.subject}\n student marks : {self.marks}\n student grade : {' '.join(self.grade)}" )
key = int(input("you start program prss 1 or exit program prass 0: "))
if key == 0:
    print("thaks for joining us")
if key == 1:
    m = int(input("how many student you add : " ))
    while m > 0 :
        m=m-1
        student_name = input("student name : ")
        subject = input("subject: ")
        marks = int(input("marks: "))
        x = student(student_name,subject,marks)
        x.student_detels()
        print("\n")
