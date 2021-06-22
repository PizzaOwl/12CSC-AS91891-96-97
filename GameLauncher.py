from tkinter import *
import os

class LogInStarter:

     def sign_up_launch(self):
        self.side_bar.destroy()
        self.log_window_frame.destroy()
        Signup(root)

     def __init__(self, parent):
        BackgroundColour = "#1a2b2c"

        self.log_username_var = StringVar()
        self.log_password_var = StringVar()

        self.side_bar = Frame(parent, bg = BackgroundColour, width = 125, height = 150, relief = 'sunken',borderwidth = 2, )
        self.side_bar.pack(expand = False, fill = 'both', side = 'left', anchor = 'nw')

        #creating the frame
        self.log_window_frame = Frame(parent, bg = BackgroundColour,padx = 175,pady = 150)
        self.log_window_frame.pack(expand = False, fill = 'both', side = 'right', anchor = 'ne')

        self.heading_label = Label(self.log_window_frame, text = "Log-In",bg = BackgroundColour, fg  =  "#7fb643")
        self.heading_label.pack(anchor = 'center', side = 'top',padx = 20)


        self.log_username_box = Entry(self.log_window_frame, textvariable = self.log_username_var ,bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Username")#creating an input box
        self.log_username_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5) 

        self.log_password_box = Entry(self.log_window_frame, textvariable = self.log_password_var ,bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Password")#creating an input box
        self.log_password_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5)

        self.sign_up_button = Button(self.log_window_frame, text = "Sign up",bg = "#8bc4d9", command = self.sign_up_launch)#now were making a button
        self.sign_up_button.pack(anchor = 'center', side = 'top',padx = 20,pady = 10)

        self.log_in_button = Button(self.log_window_frame, text = "Log In",bg = "#8bc4d9",command = self.main_menu_launch)#now were making a button
        self.log_in_button.pack(anchor = 'center', side = 'top',padx = 20,pady = 10)

        self.heading_label = Label(self.log_window_frame, text = "",bg = '#1a2b2c', fg  =  "#7fb643")
        self.heading_label.pack(anchor = 'center', side = 'top',padx = 20) 

     def main_menu_launch(self): 
        user_log = open(os.path.join(sys.path[0],r"UserLog.txt"))
        user_login_info = self.log_username_var.get() + '  ' + self.log_password_var.get()
        if user_login_info in user_log.read():
            user_log.close
            self.side_bar.destroy()
            self.log_window_frame.destroy()
            MainMenu(root)
        else:
            self.heading_label.configure(text = "Invalid input, please try again or sign up")
            user_log.close


class Signup:
    def __init__(self, parent):
        BackgroundColour = "#1a2b2c"
        
        self.username_var = StringVar()

        self.sign_window_frame = Frame(parent, bg = BackgroundColour,padx = 300,pady = 300)
        self.sign_window_frame.grid(row=0, column=1)

        self.heading_label = Label(self.sign_window_frame, text = "Sign-Up",bg = BackgroundColour, fg  =  "#7fb643", font = "courier")
        self.heading_label.grid(row=1, column=1, padx=20, pady=20)  

        self.username_label = Label(self.sign_window_frame, text = "Username:",bg = BackgroundColour, fg  =  "#7fb643", font = "courier")
        self.username_label.grid(row=2, column=0, padx=20, pady=20)

        self.username_box = Entry(self.sign_window_frame, textvariable = self.username_var, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier")#creating an input box
        self.username_box.grid(row=2, column=1, padx=20, pady=20)

        self.username_confirm_button = Button(self.sign_window_frame,text = "Continue",bg = "#8bc4d9",command = self.password_sign_up)
        self.username_confirm_button.grid(row=3, column=1, padx=20, pady=20)
              
    def password_sign_up(self):
        self.username_label.destroy()
        self.username_box.destroy()
        self.username_confirm_button.destroy()


        self.password_var = StringVar()
        self.confirm_password_var = StringVar()

        self.confirm_password_var.trace('w', self.validate)


        self.message_label = Label(self.sign_window_frame, bg = "#1a2b2c", fg  =  "#7fb643", font = "courier")
        self.message_label.grid(row=0, column=1, padx=20, pady=20)

        self.password_label = Label(self.sign_window_frame, text = "Password:",bg = "#1a2b2c", fg  =  "#7fb643", font = "courier")
        self.password_label.grid(row=1, column=0, padx=20, pady=20)
        
        self.password_box = Entry(self.sign_window_frame, textvariable = self.password_var, bg = "#1f2627",fg = "#fcfaf9",insertbackground = "#82f207",insertwidth = 5,font = "courier")#creating an input box
        self.password_box.grid(row=1, column=1, padx=20, pady=20)
        self.password_box.focus()

        self.confirm_password_label = Label(self.sign_window_frame, text = "Confirm Password:",bg = "#1a2b2c", fg  =  "#7fb643", font = "courier")
        self.confirm_password_label.grid(row=2, column=0, padx=20, pady=20)

        self.confirm_password_box = Entry(self.sign_window_frame, textvariable = self.confirm_password_var, bg = "#1f2627",fg = "#fcfaf9",insertbackground = "#82f207",insertwidth = 5,font = "courier")#creating an input box
        self.confirm_password_box.grid(row=2, column=1, padx=20, pady=20)
        self.confirm_password_box.focus()

        self.create_account_button = Button(self.sign_window_frame,text = "Create Account",bg = "#8bc4d9",command = self.create_account)
        self.create_account_button.grid(row=3, column=1, padx=20, pady=20)

    def confirm_message(self, message, type = None):
        self.message_label['text'] = message
        if type:
            self.message_label['style'] = type

    def validate(self, *args):
        validate_password = self.password_var.get()
        validate_confirm_password = self.confirm_password_var.get()

        if validate_confirm_password == validate_password:
            self.confirm_message("Success: Password matches")
            return

        elif validate_password.startswith(validate_confirm_password):
            self.confirm_message ("Warning: Password does not match yet")

        else:
            self.confirm_message("Error: Password does not match")

    def create_account(self):
        self.username_var.get()
        self.password_var.get()
        self.confirm_password_var.get() 
        os.chdir(r'C:\Coding Shenanigans\School Files\12CSC\AS91891-96-97\Version 3')  
        user_log = open(r"UserLog.txt", "a")
        user_account = self.username_var.get() + '  ' + self.password_var.get() + '\n'
        user_log.write(user_account)
        user_log.write('\n')
        user_log.close
        self.sign_window_frame.destroy()
        LogInStarter(root)


class MainMenu:
    def __init__(self, parent):
        BackgroundColour = "#1a2b2c"

        self.main_window_frame = Frame(parent, bg = BackgroundColour, width = 200, height = 300, relief = 'sunken',borderwidth = 2, )
        self.main_window_frame.pack(expand = False, fill = 'both', side = 'left', anchor = 'w')

        self.main_button_1 = Button(self.main_window_frame,text = "Start Quiz", bg = "#8bc4d9", command = self.quiz_launch)
        self.main_button_1.grid(row=0, column=1, padx=100, pady=20)

        self.main_button_2 = Button(self.main_window_frame,text = "Continue", bg = "#8bc4d9")
        self.main_button_2.grid(row=1, column=1, padx=100, pady=20)

        self.main_button_3= Button(self.main_window_frame,text = "Continue", bg = "#8bc4d9")
        self.main_button_3.grid(row=2, column=1, padx=100, pady=20)

        self.main_button_4 = Button(self.main_window_frame,text = "Continue", bg = "#8bc4d9")
        self.main_button_4.grid(row=3, column=1, padx=100, pady=20)

        self.animation_side_bar = Frame(parent, bg = BackgroundColour, width = 100, height = 175, relief = 'sunken',borderwidth = 2, )
        self.animation_side_bar.pack(expand = False, fill = 'both', side = 'bottom', anchor = 'se')

        self.log_username_box = Entry(self.animation_side_bar, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier")
        self.log_username_box.pack(anchor = 'center', side = 'top',padx = 20,pady = 5) 

        self.main_log_sidebar = Frame(parent, bg = BackgroundColour,padx = 100,pady = 125)
        self.main_log_sidebar.pack(expand = False, fill = 'both', side = 'top', anchor = 'ne')

        self.log_username_box = Entry(self.main_log_sidebar, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Username")
        self.log_username_box.pack(anchor = 'n', side = 'top',padx = 10,pady = 5) 

        self.log_password_box = Entry(self.main_log_sidebar, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Password")
        self.log_password_box.pack(anchor = 'n', side = 'top',padx = 10,pady = 5)

    def quiz_launch(self):
        self.main_log_sidebar.destroy()
        self.animation_side_bar.destroy()
        self.main_window_frame.destroy()
        Quiz(root)

if __name__ == "__main__":
  root = Tk() #creating a window
  root.title("Log-In")
  LogInInstance = LogInStarter(root)
  root.mainloop() #test
