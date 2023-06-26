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

        # For Mobile (In Customer_label Frame)
        self.lb1_mob=Label(Cust_Farame,text="Mobile No.",font=("Cosmic Sans",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Farame,font=("Cosmic Sans",10,"bold"),width=24)
        self.entry_mob.grid(row=0,column=1)

        # For Customer name(In Customer_label Frame)
        self.lb1Custname=Label(Cust_Farame,text="Customer Name",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lb1Custname.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustname=ttk.Entry(Cust_Farame,font=("Cosmic Sans",10,"bold"),width=24)
        self.txtCustname.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        # For Email field(In Customer_label Frame)
        self.lblEmail=Label(Cust_Farame,text="Email",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Farame,font=("Cosmic Sans",10,"bold"),width=24)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


         # Product_Label Frame

        Cust_Farame=LabelFrame(Main_frame,text="Product", font=("Cosmic Sans",12,"bold"),bg="white",fg="red")
        Cust_Farame.place(x=370,y=5,width=500,height=140)


if __name__ =='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()