# Hello everyone , In this video we will be creating stop watch using python 
# Importing some necessary libraries
import tkinter as Tkinter

from datetime import datetime

counter=0
running=False

def counter_label(label):
    def count():
        if running:
            global counter
    # To manage the initial play
            if counter==0:
                display='Ready'
            else:
                tt=datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display=string
            label['text']=display

            # label.after(arg1,arg2) delays by first argument given in milliseconds and then
            # calls the function given as second argument , Generally like here we need to call the 
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds call cont again.
            label.after(1000,count)
            counter += 1
    # Triggering the start of the counter
    count()  

# Start the function of stop watch

def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

# Stop function of watch
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False
# Reset function for stopwatch
def Reset(label):
    global counter
    counter=0
    # If reset is pressed after pressing stop
    if not running:
        reset['state']='disabled'
        label['text']='00:00:00'
    # If reset is pressed while the stopwatch is running
    else:
        label['text']='00:00:00'

# Adding Graphics interface
root=Tkinter.Tk()
root.title("Stop Watch")

# Fixing the window size
root.minsize(width=250,height=80)
label=Tkinter.Label(root, text='Ready!',fg='black', font='Veranda 30 bold')
label.pack()
f=Tkinter.Frame(root)
start=Tkinter.Button(f, text='Start',width=6, command=lambda: Start(label))
stop=Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset=Tkinter.Button(f, text='Reset', width=6, state='disabled', command= lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()
# Let's run this raw code
# Lets run it again
# SOurce code will be provided to pin comment
# Don't forget to like share and subscribe

# Let's convert it into .exe format

