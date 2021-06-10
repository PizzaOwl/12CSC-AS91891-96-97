from tkinter import *

Username = []
Password = []

class LogInStarter:

    def sign_up_launch(self):
        self.side_bar.destroy()
        self.log_window_frame.destroy()
        Signup(root)

    def main_menu_launch(self):
        self.side_bar.destroy()
        self.log_window_frame.destroy()
        MainMenu(root)

    def __init__(self, parent):
        BackgroundColour = "#1a2b2c"

        self.side_bar = Frame(parent, bg = BackgroundColour, width = 150, height = 100, relief = 'sunken',borderwidth = 2, )
        self.side_bar.pack(expand = False, fill = 'both', side = 'left', anchor = 'nw')

        #creating the frame
        self.log_window_frame = Frame(parent, bg = BackgroundColour,padx = 100,pady = 100)
        self.log_window_frame.pack(expand = False, fill = 'both', side = 'right', anchor = 'ne')

        self.heading_label = Label(self.log_window_frame, text = "Log-In",bg = BackgroundColour, fg  =  "#7fb643")
        self.heading_label.pack(anchor = 'center', side = 'top',padx = 20)#create label to ask for the users name  

        self.log_username_box = Entry(self.log_window_frame, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Username")#creating an input box
        self.log_username_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5) 

        self.log_password_box = Entry(self.log_window_frame, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Password")#creating an input box
        self.log_password_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5)

        self.sign_up_button = Button(self.log_window_frame,text = "Sign up",bg = "#8bc4d9", command = self.sign_up_launch)#now were making a button
        self.sign_up_button.pack(anchor = 'center', side = 'top',padx = 20,pady = 10)

        self.log_in_button = Button(self.log_window_frame,text = "Log In",bg = "#8bc4d9",command = self.main_menu_launch)#now were making a button
        self.log_in_button.pack(anchor = 'center', side = 'top',padx = 20,pady = 10)

class Signup:

    ERROR = 'Error.Label'
    SUCCESS = 'Success.Label'

    def __init__(self, parent):
        BackgroundColour = "#1a2b2c"

        self.sign_window_frame = Frame(parent, bg = BackgroundColour,padx = 100,pady = 100)
        self.sign_window_frame.grid(row=0, column=1)

        self.heading_label = Label(self.sign_window_frame, text = "Sign-Up",bg = BackgroundColour, fg  =  "#7fb643")
        self.heading_label.grid(row=1, column=1, padx=20, pady=20)  

        self.username_label = Label(self.sign_window_frame, text = "Username:",bg = BackgroundColour, fg  =  "#7fb643")
        self.username_label.grid(row=2, column=0, padx=20, pady=20)

        self.username_box = Entry(self.sign_window_frame, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Username")#creating an input box
        self.username_box.grid(row=2, column=1, padx=20, pady=20)

        self.confirm_button = Button(self.sign_window_frame,text = "Continue",bg = "#8bc4d9",command = self.passwordsignup)
        self.confirm_button.grid(row=3, column=1, padx=20, pady=20)

    def passwordsignup(self):
        self.username_label.destroy()
        self.username_box.destroy()
        self.confirm_button.destroy()
        

        self.password_var = StringVar()
        self.confirm_password_var = StringVar()

        self.confirm_password_var.trace('w', self.validate)


        self.message_label = Label(self.sign_window_frame)
        self.message_label.grid(row=0, column=1, padx=20, pady=20)
        
        self.password_box = Entry(self.sign_window_frame, textvariable = self.password_var, bg = "#1f2627",fg = "#fcfaf9",insertbackground = "#fcfaf9",insertwidth = 5,font = "courier")#creating an input box
        self.password_box.grid(row=1, column=1, padx=20, pady=20)
        self.password_box.focus()

        self.confirm_password_box = Entry(self.sign_window_frame, textvariable = self.confirm_password_var, bg = "#becccc",fg = "#fcfaf9",insertbackground = "#fcfaf9",insertwidth = 5,font = "courier")#creating an input box
        self.confirm_password_box.grid(row=2, column=1, padx=20, pady=20)
        self.confirm_password_box.focus()
    
    def confirmmessage(self, message, type = None):
        self.message_label['text'] = message
        if type:
            self.message_label['style'] = type

    def validate(self, *args):
        validatepassword = self.password_var.get()
        validateconfirmpassword = self.confirm_password_var.get()

        if validateconfirmpassword == validatepassword:
            self.confirmmessage("Success: Password matches")
            return

        elif validatepassword.startswith(validateconfirmpassword):
            self.confirmmessage ("warning")("Error: Password")

        else:
            self.confirmmessage("Error: Password does not match")



    class MainMenu:
        def __init__(self, parent):
            BackgroundColour = "#1a2b2c"

            self.Sidebar = Frame(parent, bg = BackgroundColour, width = 150, height = 100, relief = 'sunken',borderwidth = 2, )
            self.Sidebar.pack(expand = False, fill = 'both', side = 'left', anchor = 'nw')

            #creating the frame
            self.window_frame = Frame(parent, bg = BackgroundColour,padx = 100,pady = 100)
            self.window_frame.pack(expand = False, fill = 'both', side = 'right', anchor = 'ne')

class MainMenu:
    def __init__(self, parent):
        BackgroundColour = "#1a2b2c"

        self.main_side_bar = Frame(parent, bg = BackgroundColour, width = 200, height = 100, relief = 'sunken',borderwidth = 2, )
        self.main_side_bar.pack(expand = False, fill = 'both', side = 'left', anchor = 'nw')

        self.animation_side_bar = Frame(parent, bg = BackgroundColour, width = 100, height = 125, relief = 'sunken',borderwidth = 2, )
        self.main_side_bar.pack(expand = False, fill = 'both', side = 'right', anchor = 'se')

        self.log_username_box = Entry(self.animation_side_bar, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Username")#creating an input box
        self.log_username_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5) 

        #creating the frame
        self.main_window_frame = Frame(parent, bg = BackgroundColour,padx = 100,pady = 100)
        self.main_window_frame.pack(expand = False, fill = 'both', side = 'right', anchor = 'ne')

        self.log_username_box = Entry(self.main_window_frame, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Username")#creating an input box
        self.log_username_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5) 

        self.log_password_box = Entry(self.main_window_frame, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Password")#creating an input box
        self.log_password_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5)


if __name__ == "__main__":
  root = Tk() #creating a window
  root.title("Log-In")
  LogInInstance = LogInStarter(root)
  root.mainloop() #test
