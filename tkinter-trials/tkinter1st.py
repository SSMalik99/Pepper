#New program
# import tkinter
# root=tkinter.Tk()# root is a master
# root.title("login")
# left,top,width,height=0,0,410,310#error in both type of geometry
# # strPosition=str(width)+"x"+str(height)+ "+"+str(left)+ "+"+str(top)
# # root.geometry(strPosition)
# # root.geometry("400x300+0+0")
# """how to provide dimension to the root using:-
# root.geometry(width x height + left + top)
# """
# #let's make this root moving.
# def runTk():
#     global left,top,width,height
#     strPosition = str(width) + "x" + str(height) + "+" + str(left) + "+" + str(top)
#     root.geometry(strPosition)
#     left+=10
#     top+=10
#     root.after(100,runTk)
# root.after(100,runTk)
# root.mainloop() #mainloop is a function
# print("yes it is working")


# New program
import tkinter
def login_validate(email,passwod):
    if(email=="abc@abc.com" and passwod=="xyz"):
        print("you are valid")
    else:
        print("you are not valid")
def btn_login_click():
    email=en_email.get()
    password=en_password.get()
    login_validate(email,password)
root=tkinter.Tk()
# root.maxsize(100,100)
# root.minsize(100,100)
root.title("Login Page")
lbl_email=tkinter.Label(master=root,text="email")
lbl_email.grid(row=0,column=0)
en_email=tkinter.Entry(master=root)
en_email.grid(row=0,column=1)
lbl_password=tkinter.Label(master=root,text="Password")
lbl_password.grid(row=1,column=0)
en_password=tkinter.Entry(master=root)
en_password.grid(row=1,column=1)
btn_login=tkinter.Button(master=root,text="Login",bg="white",width=15,command=btn_login_click)
btn_login.grid(row=2,column=2)
root.mainloop()