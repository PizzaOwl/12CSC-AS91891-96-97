from tkinter import *
names=[]
class LogInStarter:

    def namecollection(self):
        name=self.InputBox.get()
        names.append(name)
        self.LogInFrame.destroy

    def __init__(self, parent):
        BackgroundColour="#1a2b2c"

        self.Sidebar=Frame(parent, bg=BackgroundColour, width=300, height=100, relief='sunken',borderwidth=2, )
        self.Sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

        #creating the frame
        self.LogInFrame=Frame(parent, bg=BackgroundColour,padx=100,pady=100)
        self.LogInFrame.pack(expand=False, fill='both', side='right', anchor='ne')

        self.HeadingLabel=Label(self.LogInFrame, text="Log-In",bg=BackgroundColour)
        self.HeadingLabel.pack(anchor='center', side='top',padx=20)#create label to ask for the users name  

        self.InputBox=Entry(self.LogInFrame, bg="#1f2627",fg="#fcfaf9",insertbackground="#fcfaf9",insertwidth=5,font="courier",text="Username")#creating an input box
        self.InputBox.pack(anchor='center', side='top',padx=20,pady=5) 

        self.InputBox2=Entry(self.LogInFrame, bg="#1f2627",fg="#fcfaf9",insertbackground="#fcfaf9",insertwidth=5,font="courier",text="Password")#creating an input box
        self.InputBox2.pack(anchor='center', side='top',padx=20,pady=5)

        self.Button1=Button(self.LogInFrame,text="Boop",bg="Cyan",command=self.namecollection)#now were making a button
        self.Button1.pack(anchor='center', side='top',padx=20,pady=10)



if __name__=="__main__":
  root=Tk() #creating a window
  root.title("Log-In")
  LogInInstance=LogInStarter(root)
  root.mainloop() #test