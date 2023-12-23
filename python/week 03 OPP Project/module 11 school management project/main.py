from school import School,ClassRoom,Subject
from persons import Student,Teacher
def main():
    school = School('youhani', 'gazza')
    eight = ClassRoom('eight')
    school.add_classroom(eight)
    nine = ClassRoom('nine')
    school.add_classroom(nine)
    ten = ClassRoom('ten')
    school.add_classroom(ten)

    abul = Student('abir khan',eight)
    school.student_admission(abul)
    babul = Student('babul khan',eight)
    school.student_admission(babul)
    modon = Student('modon khan',eight)
    school.student_admission(modon)
    # subjects
    physics_teacher =Teacher('topon')
    physics = Subject('physics',physics_teacher)
    eight.add_subject(physics)
    chemistry_teacher =Teacher('haradon')
    chemistry = Subject('chemistry',chemistry_teacher)
    eight.add_subject(chemistry)
    
    biology_teacher =Teacher('azmol sar')
    biology = Subject('biology',biology_teacher)
    eight.add_subject(biology)
    eight.take_samster_final()
    print(school)






if __name__ == '__main__':
    main()