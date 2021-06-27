from tkinter import *
import os
import random

questions_answers = {
    1: ["What Started World War 1?", "German invasion of Poland", "French attack through Belgium", "Assasination of Franz Ferdinand", "Assasination of Franz Ferdinand", 3
    ],
    2: ["In what fortress did the legendary “Attack of the dead men” occur in", "Osoweic Fortress", "Fort Douaumont", "Konigstein Fortress", "Osoweic Fortress", 1
    ],
    3: ["What was the first country that used gas in world war 1?", "German Empire", "Russian Empire", "Ottoman Empire", "German Empire", 1
    ],
    4: ["What was the main form of warfare that was most commonly seen in world war", "Asymmetric Warfare", "Trench Warfare", "Guerrilla Warfare", "Trench Warfare", 2
    ],
    5: ["What is the name of the legendary WW1 Ace “The Red Baron”?", "Paul Billik", "Oswald Boelcke", "Manfred von Richthofen", "Manfred von Richthofen", 3
    ],
    6: ["What was the dominant naval Ship-Class used in WW1?", "Aircraft Carriers", "Dreadnoughts", "Destroyers", "Dreadnoughts",  2
    ],
    7: ["What type of infantry weapon was most commonly used in WW1?", "Muzzle Loading Rifles", "Bolt Action Rifles", "Self-loading Rifles" , "Bolt Action Rifles", 2
    ],
    8: ["What was the main role for aircraft in WW1?", "Bombing", "Anti-Air", "Reconnaissance", "Reconnaissance", 3
    ],
    9: ["What was the first nation to deploy tanks?", "Britain", "Germany", "France", "Britain", 1
    ],
    10: ["Whp was the best sniper of WW1?", "Chris Kyle", "Simo Hayha", "Francis Pegahmagabow", "Francis Pegahmagabow", 3
    ]
}
asked = []
score = 0
background_colour = "#1a2b2c"
text_box_colour = "#1f2627"
button_colour = "#8bc4d9"

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
            print(user_login_info)
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

        self.log_username_box = Entry(self.main_window_frame, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Username")
        self.log_username_box.pack(anchor = 'n', side = 'top',padx = 10,pady = 5) 

        self.log_password_box = Entry(self.main_window_frame, bg = "#1f2627",fg = "#7fb643",insertbackground = "#82f207",insertwidth = 5,font = "courier",text = "Password")
        self.log_password_box.pack(anchor = 'n', side = 'top',padx = 10,pady = 5)

        self.main_button_1 = Button(self.main_window_frame,text = "Start Quiz", bg = "#8bc4d9", command = self.quiz_launch)
        self.main_button_1.pack(anchor = 'n', side = 'top', padx=100, pady=20)


    def quiz_launch(self):
        self.main_window_frame.destroy()
        Quiz(root)

    def quiz_launch(self):
        self.main_log_sidebar.destroy()
        self.main_window_frame.destroy()
        Quiz(root)

#class to controQul window for questions.
class Quiz:

    #function to make answer buttons and question text box update with each new question.
    def question_setup(self):
      randomiser()
      self.choice_variable.set(0)
      self.question_label.config(text  = questions_answers[qnum][0])
      self.answer_1.config(text = questions_answers[qnum][1])
      self.answer_2.config(text = questions_answers[qnum][2])
      self.answer_3.config(text = questions_answers[qnum][3])
      self.quiz_continue.config(text = "Confirm")

    #function to check if the user has inputted the correct answer, manage score, and progress questions.
    def test_progress(self):
      global score
      score_display = self.score_label
      choice = self.choice_variable.get()
      if len(asked) > 9:
        if choice == questions_answers[qnum][5]:
          score += 1
          score_display.configure(text = score)
          self.quiz_frame.destroy()
          EndScreen(root)
        else:
          print(choice)
          score += 0
          score_display.configure(text = "The correct answer was: " + questions_answers[qnum][4])
          self.quiz_continue.config(text = "Confirm")
          self.quiz_frame.destroy()
          EndScreen(root)
      else:
        if choice == 0:
          self.quiz_continue.config(text = "Try Again, You didn't select an option")
          choice = self.choice_variable.get()
        else:
          if choice == questions_answers[qnum][5]:
            score += 1
            score_display.configure(text = score)
            self.question_setup()
          else:
            print(choice)
            score += 0
            score_display.configure(text = "The correct answer was: " + questions_answers[qnum][4])
            self.quiz_continue.config(text = "Confirm")
            self.question_setup()

    #function to create window for questions and answers.
    def __init__(self, parent):
      randomiser()

      self.quiz_frame = Frame(parent, background = background_colour, padx = 150, pady = 170)
      self.quiz_frame.grid()

      self.question_label = Label(self.quiz_frame, text = questions_answers[qnum][0], background = text_box_colour, borderwidth = 2, relief = "raised", height = 3, width = 40)
      self.question_label.grid(row = 0, padx = 10, pady = 10)

      self.choice_variable = IntVar()

      self.radio_button_1 = Radiobutton(self.quiz_frame, background = text_box_colour, value = 1, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button_1.grid(row = 2, sticky = W, pady = 3)

      self.answer_1 = Label(text = questions_answers[qnum][1], background = text_box_colour, borderwidth = 2, relief = "raised")
      self.answer_1.place(width = 200, height = 40, x = 250, y = 242)

      self.radio_button_2= Radiobutton(self.quiz_frame, background = text_box_colour, value = 2, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button_2.grid(row = 3, sticky = W, pady = 3)

      self.answer_2 = Label(text = questions_answers[qnum][2], background = text_box_colour, borderwidth = 2, relief = "raised")
      self.answer_2.place(width = 200, height = 40, x = 250, y = 292)

      self.radio_button_3 = Radiobutton(self.quiz_frame, background = text_box_colour, value = 3, padx = 10, pady = 10, variable = self.choice_variable)
      self.radio_button_3.grid(row = 4, sticky = W, pady = 3)

      self.answer_3 = Label(text = questions_answers[qnum][3], background = text_box_colour, borderwidth = 2, relief = "raised")
      self.answer_3.place(width = 200, height = 40, x = 250, y = 342)
 
      self.quiz_continue = Button(self.quiz_frame, text = "Confirm", background = button_colour , command  = self.test_progress)
      self.quiz_continue.place(width = 200, height = 40, x = 250, y = 342)

      self.score_label = Label(self.quiz_frame, text = "Score", background = background_colour)
      self.score_label.place(width = 200, height = 40, x = 250, y = 392)




#class to show endsceen with options to close program and play again
class EndScreen:

  def PlayAgain(self):
    self.final_frame.destroy()
    LogInStarter(root)

  def Leave(self):
    self.final_frame.destroy()
    ExitProgram(root)

  def __init__(self, parent):

    self.final_frame = Frame(parent, background = background_colour, padx = 150, pady = 170)
    self.final_frame.grid()

    self.ending_text = Label(self.final_frame, text = "Well done, you got {} out of 10 questions right" .format(score), background = text_box_colour, borderwidth = 2, relief = "raised", height = 2, width = 50)
    self.ending_text.grid(row = 0, pady = 0, padx = 20)

    self.play_again_button = Button(self.final_frame, text = "Play Again?", background = button_colour, command = self.PlayAgain, width = 12, height = 1)
    self.play_again_button.place(x = 210, y = 60)

    self.leave_button = Button(self.final_frame, text = "Exit", background = button_colour, command = self.Leave, width = 12, height = 1)
    self.leave_button.place(x = 80, y = 60)

#class to check to make sure the user wants to close the program
class ExitProgram:

  def Cancel(self):
    self.close_frame.destroy()
    MainMenu(root)

  def Confirm(self):
    self.close_frame.destroy()
    exit()

  def __init__(self, parent):

    self.close_frame = Frame(parent, background = background_colour, padx = 150, pady = 170)
    self.close_frame.grid()

    self.confirm_text = Label(self.close_frame, text = "Are you sure you want to exit?", background = text_box_colour, borderwidth = 2, relief = "raised", height = 2, width = 30)
    self.confirm_text.grid(row = 0, pady = 0, padx = 20)

    self.confirm_button = Button(self.close_frame, text = "Confirm", background = button_colour, command = self.Confirm, width = 10, height = 1)
    self.confirm_button.place(x = 140, y = 60)

    self.cancel_button = Button(self.close_frame, text = "Cancel", background = button_colour, command = self.Cancel, width = 10, height = 1)
    self.cancel_button.place(x = 30, y = 60)

def questions_setup(self):
  randomiser()
  self.choice_variable.set(0)
  self.question_label.config(text  = questions_answers[qnum][0])
  self.answer_1.config(text = questions_answers[qnum][1])
  self.answer_2.config(text = questions_answers[qnum][2])
  self.answer_3.config(text = questions_answers[qnum][3])

def randomiser():
  global qnum
  qnum = random.randint(1, 10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()

if __name__ == "__main__":
  root = Tk() #creating a window
  root.title("Log-In")
  LogInInstance = LogInStarter(root)
  root.mainloop() #test
