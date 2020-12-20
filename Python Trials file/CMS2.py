# CMS using OOPs
#BLL
"this module is made for customer management system"
import json
class Customer:
    cuslist=[]  #static
    def convtodict(obj):
        return obj.__dict__
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
        self.email=0
    def addCustomer(self):
        "will add new customer inside the data"
        Customer.cuslist.append(self)
        file1=open("E://bubby/file_handling1/CMS_json.txt","w+")
        json.dump(Customer.cuslist,file1,default =Customer.convtodict)
    def modcustomer(self):
        "will modify a customer"
        for e in Customer.cuslist:
            if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.email=self.email
                return e
            else:
                print("there is no customer with this id")
    def search_customer(self):
        "will search a customer insidr the available data"
        for e in Customer.cuslist:
            if(e.id==self.id):
                showcustomer(e)
                return
    @staticmethod
    def delete_customer(self):
        "this method is a static method to delete a customer"
        for e in Customer.cuslist:
            if(e.id==self.id):
                Customer.cuslist.remove(e)
                return
#PL
def showcustomer(cus):
    "this function will show the customer"
    print("customer id:",cus.id,"customer name:",cus.name,"customer age:",cus.age,
          "customer mobile number:",cus.mob,"customer email id:",cus.email)
# def getid():
#     x=0
#     if(len(Customer.cuslist)==0):
#         cus.id=1
#     else:
#         cus.id=x+1
#     x+=1
def getname():
    "this function is used to det the proper name"
    while(1):
        cus.name=input("enter customer name:")
        if(cus.name.isalpha()):
            return cus.name
        else:
            print("only alphabets are allowed in Name")
def getmob():
    "this method will take proper mobile number of a customer"
    while(1):
        cus.mob=input("enter customer mobile number:")
        if(cus.mob.isnumeric()):
            if(len(cus.mob)==10):
                return cus.mob
            else:
                print("mobile number should atleast 10 numbers")
        else:
            print("only numbers are allowed in mobile number")
def getage():
    "this will take the specific age of the customer"
    while(1):
        cus.age=input("enter customer age:")
        if(cus.age.isnumeric()):
            if(16<=int(cus.age)<=60):
                return cus.age
            else:
                print("customer age must be between 16 and 60 years")
        else:
            print("age must be numeric")
if(__name__=="__main__"):
    while(1):
        print("1 for add customer,2 for modify customer detail,3 for search customer"
              "4 to delete customer 5 to show all customer  6 to exxit from the process")
        choice = input("enter your choice").strip()  # give what user want to do
        if(choice=="1"):
            cus=Customer()
            cus.id=input("enter id of customer:")
            cus.name=getname()
            cus.age=getage()
            cus.mob=getmob()
            cus.email=input("enter email id of customer:")
            cus.addCustomer()
            print("customer added successfully")
        elif(choice == "2"):
            cus=Customer()
            cus.id=input("enter the id of customer")
            cus.name=input("enter updated name of customer")
            cus.age=input("enter updated age of customer")
            cus.mob=input("enter updated mobile number of customer")
            cus.email=input("enter updated email id of customer")
            cus.modcustomer()
            print("customer details updated successfully")
        elif(choice=="3"):
            cus=Customer()
            cus.id=input("enter the id of customer:")
            cus.search_customer()
        elif(choice=="4"):
            cus=Customer()
            cus.id=input("enter the id of customer:")
            Customer.delete_customer()
            print("customer deleted successfully")
        elif(choice=="5"):
            cus=Customer()
            for e in Customer.cuslist:
                showcustomer(e)
        elif(choice=="6"):
            break
        else:
            print("please enter correct choice")