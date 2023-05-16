from tkinter import *
from tkinter import messagebox
import time
import sys
from pygame import mixer
from PIL import Image, ImageTk

def alarm():
    alarm_time = user_input_time.get()
    alarm_message = user_input_message.get()

    if alarm_time == "":
        messagebox.askretrycancel("Invalid Time Format", "Please Enter Time Value")
    elif alarm_message == "":
        messagebox.askretrycancel("Please Enter a valid Message")
    else:
        current_time = time.strftime("%H:%M")
        if current_time >= alarm_time:
            messagebox.showinfo("Alarm", alarm_message)
            playmusic()
        else:
            time_diff = time.mktime(time.strptime(alarm_time, "%H:%M")) - time.mktime(time.strptime(current_time, "%H:%M"))
            root.after(int(time_diff*1000), lambda: alarm_callback(alarm_message))

def alarm_callback(alarm_message):
    messagebox.showinfo("Alarm", alarm_message)
    playmusic()

def playmusic():
    mixer.init()
    mixer.music.load('alarm.mp3')
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(1)

    mixer.music.stop()
    sys.exit()


root = Tk()
root.title("Alarm Clock")
root.geometry("1024x768")
canvas = Canvas(root, width=1024, height=768)
image = ImageTk.PhotoImage(Image.open("alarm.png"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

header = Frame(root)

box1 = Frame(root)
box1.place(x=100, y=100)

box2 = Frame(root)
box2.place(x=70, y=170)

# Time taken by User as Input
user_input_time = Entry(box1, font=('Times New Roman', 20), width=8)
user_input_time.grid(row=0, column=1)

# Label for Time Input
time_label = Label(box1, text="Enter Time (HH:MM)", font=('Times New Roman', 14))
time_label.grid(row=0, column=0)

# Message taken by User as Input
user_input_message = Entry(box2, font=('Times New Roman', 20), width=20)
user_input_message.grid(row=1, column=1)

# Label for Message Input
message_label = Label(box2, text="Enter Label ", font=('Times New Roman', 14))
message_label.grid(row=1, column=0)

# Set Alarm Button
start_button = Button(box2, text="Set Alarm", font=('Times New Roman', 16, 'bold'), command=alarm)
start_button.grid(row=3, column=1)

root.mainloop()
