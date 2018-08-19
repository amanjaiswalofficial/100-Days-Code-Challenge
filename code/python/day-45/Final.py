from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.title("Recog: Face Recognition Based Attendance")
root.geometry("800x600")
root.state('zoomed')
#root.attributes('-fullscreen', True) full screen, no title bar


class Example(Frame):#note example word used instead of Window, no problem
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)


        self.image = Image.open("./layout/bgone.png")#set the background
        self.img_copy = self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

        #two labels, for notification and attendance defined globally
        self.label1 = Label(self, text="First Label", font=(
            "Helvetica", 18), width=0, height=0, fg="#444444")
        self.label1.place(x=485, y=315)
        self.label1.config(bg="White")
        self.label2 = Label(self, text="Second Label", font=(
            "Helvetica", 18), width=0, height=0, fg="#444444")
        self.label2.place(x=485, y=507)
        self.label2.config(bg="White")


        self.showHeader()
        self.takeImageBtn()
        self.trainImageBtn()
        self.trackImageBtn()
        self.quitBtn()
        self.clearID()
        self.clearName()
        self.showLabels()
        self.showText()
        

    #clear Button
    def clearID(self):
        image = PhotoImage(file="./layout/clearid.png")
        qbtn = Button(self, text="Clear ID", width=124, height=44,command=self.clearvalid)
        qbtn.config(image=image)
        qbtn.image = image  # real button definition
        qbtn.place(x=830, y=200)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)
    
    #function that will clear the value
    def clearvalid(self):
        Example.text1.delete(1.0, END)


    #clear name button
    def clearName(self):
        image = PhotoImage(file="./layout/clearname.png")
        qbtn = Button(self, text="Clear Name", width=124, height=44,command=self.clearvalname)
        qbtn.config(image=image)
        qbtn.image = image  # real button definition
        qbtn.place(x=830, y=255)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)
    
    #function that will clear the name value
    def clearvalname(self):
        Example.text2.delete(1.0, END)

    #function to display textboxes
    def showText(self):
        Example.text1 = Text(width=18, height=1, font=("Helvetica", 24))
        Example.text1.pack()
        Example.text1.place(x=488, y=200)
        Example.text2 = Text(width=18, height=1, font=("Helvetica", 24))
        Example.text2.pack()
        Example.text2.place(x=488, y=250)

    #function to display all labels
    def showLabels(self):
        load=Image.open("./layout/label_one.png")
        render=ImageTk.PhotoImage(load)
        img=Label(self,text="Enter ID",image=render,width=90,height=40)
        img.image=render
        img.place(x=383,y=200)

        load = Image.open("./layout/label_two.png")
        render = ImageTk.PhotoImage(load)
        img2 = Label(self, text="Enter Name",image=render, width=138, height=38)
        img2.image = render
        img2.place(x=338, y=250)

        load = Image.open("./layout/notification.png")
        render = ImageTk.PhotoImage(load)
        img3 = Label(self, text="Notification",image=render, width=138, height=35)
        img3.image = render
        img3.place(x=338, y=310)

        load = Image.open("./layout/attendance.png")
        render = ImageTk.PhotoImage(load)
        img2 = Label(self, text="Attendance",image=render, width=138, height=35)
        img2.image = render
        img2.place(x=338, y=500)


    #take image button
    def takeImageBtn(self):
        image=PhotoImage(file="./layout/capture.png")
        qbtn = Button(self, text="Take Image",width=150,height=50)
        qbtn.config(image=image)
        qbtn.image=image  # real button definition
        qbtn.place(x=245.75, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)
    

    #Example of changing text by clicking a button, can be set on anything else as well
    def trainImageBtn(self):
        image=PhotoImage(file="./layout/train.png")
        qbtn = Button(self, text="Train Image",width=150,height=50,command=self.trainBtnAction)
        qbtn.config(image=image)
        qbtn.image=image  # real button definition
        qbtn.place(x=487, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)

    #now on clicking sets the new text in the labels, can be changed
    def trainBtnAction(self):
        print(self.label1['text'])#set text by using = and the text to display
        print(self.label2['text'])
        self.label1['text']="Changed first label"
        self.label2['text']="Changed second label"
        
        
    #track image button
    def trackImageBtn(self):
        image=PhotoImage(file="./layout/track.png")
        qbtn = Button(self, text="Track Image",width=150,height=50)
        qbtn.config(image=image)
        qbtn.image=image  # real button definition
        qbtn.place(x=728.5, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack()

    #quit button
    def quitBtn(self):
        image = PhotoImage(file="./layout/quit.png")
        qbtn = Button(self, text="Quit", width=150, height=50,command=exit)
        qbtn.config(image=image)
        qbtn.image = image  # real button definition
        qbtn.place(x=970, y=400)
        self.master.title("GUI")  # name of the window, should be outside
        self.pack(fill=BOTH, expand=1)

    #function to show title of the project: Fusion
    def showHeader(self):#for the fusion title
        load = Image.open("./layout/header.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=383, y=0)

    def _resize_image(self, event):#to have bg resized as you adjust the window

        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


e = Example(root)
#e.pack(fill=BOTH, expand=YES)
root.mainloop()
