from tkinter import * #import all classes and libraries from tkinter
import RPi.GPIO as GPIO #import RPi.GPIO and rename it as GPIO
import time
GPIO.setmode(GPIO.BCM) # set GPIO in BCM numbering
GPIO.setup(18,GPIO.OUT) #set GPIO 18 as output
pwm = GPIO.PWM(18,500) #sets the PWM frequency of 500Hz

pwm.start(100) #initial pwm value =100
class App:
    def __init__(self,master):
        frame = Frame(master) #create  a frame widget as container
        frame.pack(pady = 200)          #pack the frame into main window
        scale = Scale(frame,from_ = 0, to = 100,fg = 'blue',bg = 'white', orient = VERTICAL, command = self.update)
        scale.grid(padx = 5, pady = 5) #place the checkbox in the frame using grid layout
    def update(self, duty):
        pwm.ChangeDutyCycle(float(duty))
root = Tk()     #create a main window
root.configure(bg = "lightgreen")
root.wm_title('PWM Power Control')  #sets window title "PWM Power Control"
app = App(root)   #passing main window as master
root.geometry("200x50+0+0")  #window size to 200x50 px and Pos to top left corner
root.mainloop() #start tkinter main loop
