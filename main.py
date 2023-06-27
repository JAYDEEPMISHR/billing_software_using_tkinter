from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  # pip install pillow



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Billing System")

        # Image 1
        # img=Image.open("Images/download.jpeg")
        # img=img.resize((500,130),Image.ANTIALIAS)
        # self.photoimg= ImageTk.PhotoImage(img)

        # lb1_img=Label(self.root,image=self.photoimg)
        # lb1_img.place(x=0,y=0,width=500,height=130)    

        lb1_title=Label(self.root, text="BILLING SOFTWARE", font=("Cosmic Sans",35,"bold"),bg="white", fg="red")
        lb1_title.place(x=0, y=0, width=1320, height=45)

        Main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        Main_frame.place(x=0,y=45,width=1920,height=620)

# Customer_Label Frame

        Cust_Farame=LabelFrame(Main_frame,text="Customer", font=("Cosmic Sans",12,"bold"),bg="white",fg="red")
        Cust_Farame.place(x=7,y=5,width=270,height=140)

        # For Mobile (In Customer_label Frame)
        self.lb1_mob=Label(Cust_Farame,text="Mobile No.",font=("Cosmic Sans",12,"bold"),bg="white")
        self.lb1_mob.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Farame,font=("Cosmic Sans",10,"bold"),width=20)
        self.entry_mob.grid(row=0,column=1)

        # For Customer name(In Customer_label Frame)
        self.lb1Custname=Label(Cust_Farame,text="Name",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lb1Custname.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txtCustname=ttk.Entry(Cust_Farame,font=("Cosmic Sans",10,"bold"),width=20)
        self.txtCustname.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        # For Email field(In Customer_label Frame)
        self.lblEmail=Label(Cust_Farame,text="Email",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblEmail.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Farame,font=("Cosmic Sans",10,"bold"),width=20)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


# Product_Label Frame
        Product_frame=LabelFrame(Main_frame,text="Product", font=("Cosmic Sans",12,"bold"),bg="white",fg="red")
        Product_frame.place(x=280,y=5,width=480,height=140)

        # For Category Label(In Product_label)
        self.lblCategory=Label(Product_frame,text="Select Category",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblCategory.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_frame,font=("Cosmic Sans",12,"bold"),width=12,state="readonly")
        self.Combo_Category.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        # For Subcategory label(In Product_label)
        self.lblSubCategory=Label(Product_frame,text="Sub Category",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblSubCategory.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_frame,font=("Cosmic Sans",12,"bold"),width=12,state="readonly")
        self.ComboSubCategory.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        # For Product name(In Product_label)
        self.lblProduct=Label(Product_frame,text="Product name",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblProduct.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_frame,font=("Cosmic Sans",12,"bold"),width=12)
        self.ComboProduct.grid(row=2,column=1,sticky=W,padx=5,pady=2)

        # For Price(In Product_label)
        self.lblPrice=Label(Product_frame,text="Price",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblPrice.grid(row=0,column=2,stick=W,padx=5,pady=2)

        self.ComboPrice=ttk.Combobox(Product_frame,font=("Cosmic Sans",12,"bold"),width=7)
        self.ComboPrice.grid(row=0,column=3,sticky=W,padx=5,pady=2)

        # For Quantity(In Product_label)
        self.lblQty=Label(Product_frame,text="Quantity",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblQty.grid(row=1,column=2,stick=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_frame,font=("Cosmic Sans",12,"bold"),width=9)
        self.ComboQty.grid(row=1,column=3,sticky=W,padx=5,pady=2)

# Middle frame for pictures

        MiddleFrame=Frame(Main_frame,bd=10)
        MiddleFrame.place(x=7,y=150,width=750,height=340)

        # Image1
        img=Image.open("Images/download.jpeg")
        img=img.resize((375,340),Image.ANTIALIAS)
        self.photoimg= ImageTk.PhotoImage(img)

        lb1_img=Label(MiddleFrame,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=375,height=340)

        # Image2
        img2=Image.open("Images/download.jpeg")
        img2=img2.resize((375,340),Image.ANTIALIAS)
        self.photoimg2= ImageTk.PhotoImage(img2)

        lb1_img2=Label(MiddleFrame,image=self.photoimg2)
        lb1_img2.place(x=375,y=0,width=375,height=340)


# Search
        Search_Frame=Frame(Main_frame,bd=2,bg="white")
        Search_Frame.place(x=760,y=10,width=500,height=40)

        self.lblBill=Label(Search_Frame,text="Bill Number",font=("Cosmic Sans",12,"bold"),fg="red",bg="white",bd=4)
        self.lblBill.grid(row=0,column=0,stick=W,padx=1)

        self.txtSearch=ttk.Entry(Search_Frame,font=("Cosmic Sans",10,"bold"),width=20)
        self.txtSearch.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,text="Search",font=("Cosmic Sans",12,"bold"), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)        

# Right side bill area
        RightLabelFrame=LabelFrame(Main_frame,text="Biiling",font=("Cosmic Sans",12,"bold"),bg="white",fg="red")
        RightLabelFrame.place(x=765,y=45,width=480,height=440)

        # Scrollbar
        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("Cosmic Sans",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

# Bottom Counter Label
        Bottom_Frame=LabelFrame(Main_frame,text="Bill Counter", font=("Cosmic Sans",12,"bold"),bg="white",fg="red")
        Bottom_Frame.place(x=0,y=485,width=1920,height=125)

        # For Subtotal(In Bottom Counter_label)
        self.lblSubTotal=Label(Bottom_Frame,text="Subtotal",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblSubTotal.grid(row=0,column=0,stick=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=("Cosmic Sans",12,"bold"),width=9)
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        # For Government tax(In Bottom Counter_label)
        self.lbl_tax=Label(Bottom_Frame,text="Gov Tax",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,font=("Cosmic Sans",12,"bold"),width=9)
        self.txt_tax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        # For Amount total with GST(In Bottom Counter_label)
        self.lblAmountTotal=Label(Bottom_Frame,text="Total",font=("Cosmic Sans",12,"bold"),bg="white",bd=4)
        self.lblAmountTotal.grid(row=2,column=0,stick=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,font=("Cosmic Sans",12,"bold"),width=9)
        self.txtAmountTotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

# Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg="white")
        Btn_Frame.place(x=320,y=0)

        # Buttons
        self.BtnAddToCart=Button(Btn_Frame,height=2,text="Add To Cart",font=("Cosmic Sans",12,"bold"), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerate_bill=Button(Btn_Frame,height=2,text="Generate Bill",font=("Cosmic Sans",12,"bold"), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnGenerate_bill.grid(row=0,column=1)

        self.BtnSave=Button(Btn_Frame,height=2,text="Save Bill",font=("Cosmic Sans",12,"bold"), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        self.BtnPrint=Button(Btn_Frame,height=2,text="Print Bill",font=("Cosmic Sans",12,"bold"), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        self.BtnClear=Button(Btn_Frame,height=2,text="Clear",font=("Cosmic Sans",12,"bold"), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        self.BtnExit=Button(Btn_Frame,height=2,text="Exit",font=("Cosmic Sans",12,"bold"), bg="orangered", fg="white",width=13,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)


if __name__ =='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()