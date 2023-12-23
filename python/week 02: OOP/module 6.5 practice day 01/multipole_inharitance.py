class company:
    def __init__(self,cname,location) -> None:
        self.cname = cname
        self.location = location

    def company_detalis(self):
        print("cmopany name = ",self.cname,"Location = ",self.location)

class person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
    def person_detels(self):
        print("name = ",self.name,"Age = ",self.age)
class employee(company,person):
    def __init__(self, emp_name,emp_age,comp_name,comp_location) -> None:
        # initialize the parent class separately.
        person.__init__(self,emp_name,emp_age)
        company.__init__(self,comp_name,comp_location)

    def detalis(self,salary,skill):
        print("salary: ",salary,"skill",skill)
#when creating an employee object,provide values for both cmmpany and person attribules
op_employee = employee("king is back",25,"solger","gaza")
op_employee.detalis(700000,"poygonist")
op_employee.company_detalis()
op_employee.person_detels()