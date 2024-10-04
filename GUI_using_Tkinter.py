from tkinter import * #imports all classes and functions from Tkinter module
import RPi.GPIO as GPIO #import the RPi.GPIO library and rename it as GPIO
import time #import the time module

GPIO.setmode(GPIO.BCM) #pin numbering system-BCM
GPIO.setup(18,GPIO.OUT) #sets GPIO18 as output

class App:
    def __init__(self,master):
        frame = Frame(master) #create a frame widget as container
        frame.pack() #pack the frame into main window
        self.check_var = BooleanVar() #create boolean variable to store checkbox state
        check = Checkbutton(frame, text = 'SW_LED1',
                            font = ("timesnewroman", 20),#font modification
                            fg = "black", bg = "lightblue", #fg and bg colours
                            command = self.update, variable = self.check_var, onvalue = True, offvalue = False)
        check.grid(row = 1) #place checkbox in the frame using grid layout
    def update(self):
        GPIO.output(18,self.check_var.get()) #sets GPIO pin 18 state to the checkbox state
        
        
root = Tk() #creates the main window
###########
root.configure(bg = "lightgrey")
###########
root.wm_title('On / Off Switch') #sets the windows title
app = App(root) #passing main window as master
root.geometry("200x50+0+0") #window size to 250x50 px and position top left corner
root.mainloop() #start Tkinter main loop