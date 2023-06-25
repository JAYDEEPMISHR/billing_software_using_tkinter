from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  # pip install pillow



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing System")

        # Image 1
        # img=Image.open("Images/download.jpeg")
        # img=img.resize((500,130),Image.ANTIALIAS)
        # self.photoimg= ImageTk.PhotoImage(img)

        # lb1_img=Label(self.root,image=self.photoimg)
        # lb1_img.place(x=0,y=0,width=500,height=130)    

        lb1_title=Label(self.root, text="BILLING SOFTWARE", font=("Cosmic Sans",35,"bold"),bg="white", fg="red")
        lb1_title.place(x=0, y=0, width=1520, height=45)

        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=45,width=1520,height=620)

        # Customer_Label Frame

        Cust_Farame=LabelFrame(Main_frame,text="Customer", font=("Cosmic Sans",12,"bold"),bg="white",fg="red")
        Cust_Farame.place(x=10,y=5,width=350,height=140)

        self.lb1_mob=Label(Cust_Farame,text="Mobile No.",font=("Cosmic Sans",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0)


if __name__ =='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()