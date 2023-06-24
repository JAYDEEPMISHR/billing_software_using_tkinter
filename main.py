from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  # pip install pillow



class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing System")

        # For image 1
        img=Image.open("Images/download.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg= ImageTk.PhotoImage(img)

        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)    

# For image 2
        img=Image.open("Images/images.jpeg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg= ImageTk.PhotoImage(img)

        lb1_img=Label(self.root,image=self.photoimg)
        lb1_img.place(x=0,y=0,width=500,height=130)





if __name__ =='__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()