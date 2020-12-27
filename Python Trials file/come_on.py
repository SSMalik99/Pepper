# class MyClass:
#     def __str__(self):
#         return "CETPA"
# ob1=MyClass()
# print(ob1)
# class C1:
#     def __init__(self):
#         self.a=8
#         self.b=7
#     def __add__(self, other):
#         res=ob1.a+ob2.c
#         return res
# class C2:
#     def __init__(self):
#         self.c=9
#         self.d=2
# ob1=C1()
# ob2=C2()
# r=ob1+ob2
# print(r)
# class c1:
#     def moc(self):
#         return "i'm public"
#     def _aoc(self):
#         return "i'm private"
#     @staticmethod
#     def __boc(self):
#         return "i'm protected"
# ob1=c1()
# res=ob1.moc()
# print(res)
# res=ob1._aoc()
# print(res)
# res=__c1.__boc()
# print(res)
"we just doing tings for joy"
# # BLL
# class C1:
#     def __init__(self):
#         self.a= 0
#         self.b= 0
#     def my_add(self):
#         self.res=self.a+self.b
#     def intg(self,):
#         if():
#             pass
#         else:
#             raise ValueError("only whole number allowed")
# # PL
# ob1=C1()
# while(1):
#     try:
#         ob1.a=input("enter 1st number:")
#         ob1.b=input("enter 1st number:")
#         ob1.intg()
#         print(ob1.res)
#     except Exception as e:
#         print("Error!",e)
#     finally:
#         ch=input("want to continue Y/N:")
#         if(ch=="N"):
#             break
# import module1
# import module2
# import module3
# print(module1.myadd(3,4))
# print(module1.mysub(3,4))
# print(module2.mymul(3,4))
# print(module2.mydiv(3,4))
# print(module3.mypow(3,4))
# print(module3.mycon(3,4))
# import pack1
# print(pack1.myadd(3,4))
# print(pack1.mysub(3,4))
# print(pack1.mymul(3,4))
# print(pack1.mydiv(3,4))
# print(pack1.mypow(3,4))
# print(pack1.mycon(3,4))
# import dic1
# # print(help(dic1))
# dic1.mysub(1,2)
# f=open("E://bubby/file_handling1/my1st.txt","r")
# data=f.read(5)
# print(data)
# print(f.tell())
# data=f.seek(6,0)
# f.close()
# import time
# f=open("E://bubby/file_handling1/my1st.txt","r")
# for i in range(5):
#     print("cetpa")
#     time.sleep(3)
# import time
# # f=open("E://bubby/file_handling1/my1st.txt","r")
# for i in range(5):
#     print("cetpa")#,flush=True)
#     time.sleep(2)

# new program
# f=open("E://bubby/file_handling1/my1st.txt","r")
# data=f.read(5)
# print(data)
# print(f.tell())
# data=f.seek(6,0)
# data=f.read()
# print(data)
# f.close()

# #New program
# f=open("E://bubby/file_handling1/my2nd.txt","w")
# # data=f.readlines()
# # print(data)
# f.write("we must have to work\n this is our first priorty")
# data=f.read()
# print(data)
# f.close()

# def delgfun(a,b,fp1,fp2):
#     res = fp1(a,b)+fp2(a,b)
#     return res
#
# def add(a,b):
#     return a+b
# def mul(a,b):
#     return a*b
# res=delgfun(3,4,add,mul)
# print(res)

# #New program
# import pickle
# f=open("E://bubby/file_handling1/my3rd.txt","wb")
# l1=[1,2,3]
# pickle.dump(l1,f)
# print("that's easy")
# f=open("E://bubby/file_handling1/my3rd.txt","rb")
# l1=pickle.load(f)
# print(l1)


# import json
# # detail_list=[1,2]
# f=open("E://bubby/file_handling1/my4th.txt","r")
# # json.dump(detail_list,f)
# # print("this may be easy")
# detail_list=json.load(f)
# print(detail_list)