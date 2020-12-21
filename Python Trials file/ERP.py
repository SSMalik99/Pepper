# ERP==Employee Resource Planning using inheritance
#BLL
class Employee():
    Cus_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addCustomer(self):
        Employee.Cus_list.append(self)
    def modCustomer(self):
        for i in Employee.Cus_list:
            if(i.id==self.id):
                if(self.designation=="Director"):
                    i.name=self.name
                    i.age=self.age
                    i.mob=self.mob
                else:
                    i.name=self.name
                    i.age=self.age
                    i.mob=self.mob
                    i.course=self.course
    def SearchCus(self):
        for e in Employee.Cus_list:
            if(e.id==self.id):
                showCus(e)
    def delCus(self):
        for e in Employee.Cus_list:
            if(e.id==self.id):
                Employee.Cus_list.remove(e)
class Director(Employee):
    def __init__(self):
        self.designation="Director"
        super().__init__()
class Manager(Employee):
    def __init__(self):
        self.designation="Manager"
        self.course=0
        super().__init__()
class Trainer(Employee):
    def __init__(self):
        self.designation="Trainer"
        self.course=0
        super().__init__()
#pL
def showCus(e):
    if(e.designation=="Director"):
        print("employee id:",e.id,"employee name:",e.name,"employee age:",e.age,
              "employee mobile number:",e.mob,"employee designation:",e.designation)
    else:
        print("employee id:", e.id, "employee name:", e.name, "employee age:", e.age,
              "employee mobile number:", e.mob, "employee designation:", e.designation,
              "employee Course:",e.course)
while(1):
    print("1 to add employee, 2 to modify employee, 3 to search employee,"
          " 4 to delete employee , 5 to show all employee,6 to exit")
    choice=input("enter your choice from 1 to 6:") #show what user want to do with the employee's detail
    if(choice=="1"):
        print("Director, Manager, Trainer")
        choice1=(input("enter the designation of the employee:").strip()).lower() #proviide datail :- about employee(about the role of employee)
        if(choice1=="director"):
            obj=Director()
            obj.id=input("enter the id of employee:")
            obj.name=input("enter the name of employee:")
            obj.age=input("enter the age of employee:")
            obj.mob=input("enter the mobile number of employee:")
            obj.addCustomer()
            print("employee added successfully")
        elif(choice1=="manager"):
            obj=Manager()
            obj.id=input("enter the id of employee:")
            obj.name=input("enter the name of employee:")
            obj.age=input("enter the age of employee:")
            obj.mob=input("enter the mobile number of employee:")
            obj.course=input("enter the course of employee:")
            obj.addCustomer()
            print("employee added successfully")
        elif(choice1=="trainer"):
            obj = Trainer()
            obj.id = input("enter the id of employee:")
            obj.name = input("enter the name of employee:")
            obj.age = input("enter the age of employee:")
            obj.mob = input("enter the mobile number of employee:")
            obj.course = input("enter the course of employee:")
            obj.addCustomer()
            print("employee added successfully")
        else:
            print("please enter designation carefully")
    elif(choice=="2"):
        choice1=input("enter id of employee:")
        for e in Employee.Cus_list:
            if(e.id==choice1):
                if(e.designation=="Director"):
                    obj=Director()
                    obj.name=input("enter updated name of employee")
                    obj.age=input("enter updated age of employee")
                    obj.mob=input("enter updated mobile number of employee")
                    obj.modCustomer()
                    print("employee's detail updated successfully")
                elif(e.designation=="Manager"):
                    obj=Manager()
                    obj.name=input("enter updated name of employee")
                    obj.age=input("enter updated age of employee")
                    obj.mob=input("enter updated mobile number of employee")
                    obj.course=input("enter updated course of employee")
                    obj.modCustomer()
                    print("employee's detail updated successfully")
                elif(e.designation=="Trainer"):
                    obj=Trainer()
                    obj.name=input("enter updated name of employee")
                    obj.age=input("enter updated age of employee")
                    obj.mob=input("enter updated mobile number of employee")
                    obj.course=input("enter updated course of employee")
                    obj.modCustomer()
                    print("employee's detail updated successfully")
                else:
                    print("entered employee's detail isn't available")
            else:
                print("entered id isn't available to modify")
    elif(choice=="3"):
        obj=Employee()
        obj.id=input("entered the id of employee:")
        obj.SearchCus()
    elif(choice=="4"):
        obj=Employee()
        obj.id=input("enter the id of employee:")
        obj.delCus()
        print("customer deleted successfully")
    elif(choice=="5"):
        for e in Employee.Cus_list:
            showCus(e)
    elif(choice=="6"):
        break
    else:
        print("enter correct choice")