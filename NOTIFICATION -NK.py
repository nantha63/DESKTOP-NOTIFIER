


#####################project title
#########################Send Desktop Notifications Using Python'''
import tkinter as tk
from tkinter import messagebox
from plyer import notification
from tkinter import*
import time

#------>using opps concept 
#using CONSTRUctor METHOD ........

# it is always called when an object of a class is created 
 
#automaticall called when object class created
#MASTER ---->OBJECT
#GET----->dictonary

class DesktopNotifier:

    def __init__(self, master):
        self.master = master
        master.title("DESKTOP NOTIFIER")
        master.geometry("1500x1500")
        master.config(bg="yellow")
        
#creating frame as window
        self.frame1=Frame(width=400,height=400,bg="blue")
        self.frame1.place(x=600,y=250)
#creating a labes 
        self.title_label = tk.Label(master, text="DESKTOP NOTIFIER",font=("times",20,"bold"),bg="cyan")
        self.title_label.place(x=650,y=200)
#creating a labes 
        self.label = tk.Label(master, text="ENTER NOTIFICATION DETAILS",font=("times",10,"bold"),bg="#000fff000")
        self.label.place(x=700,y=300)
 #creating a labes 
        self.title_label = tk.Label(master, text="TITLE",font=("times",10,"bold"),bg="cyan")
        self.title_label.place(x=700,y=350)
 #creating a entry
        self.title_entry = tk.Entry(master, width=30)
        self.title_entry.place(x=800,y=350)
 #creating a labes 
        self.message_label = tk.Label(master, text="MEASSAGE",font=("times",10,"bold"),bg="cyan")
        self.message_label.place(x=700,y=400)
 #creating a labes 
        self.message_entry = tk.Entry(master, width=30)
        self.message_entry.place(x=800,y=400)
 #creating a labes 
        self.delay_label = tk.Label(master, text="DELAY",font=("times",10,"bold"),bg="cyan")
        self.delay_label.place(x=700,y=450)
        self.delay_label = tk.Label(master, text="Developed by NANTHA KUMAR (developer)",font=("comic sans Ms",10,"bold"),bg="cyan")
        self.delay_label.place(x=300,y=650)
 #creating a entry
        self.delay_entry = tk.Entry(master, width=10)
        self.delay_entry.place(x=800,y=450)
 #creating a button
        self.notify_button = tk.Button(master, text="NOTIFI  ME!!!!!!!!", command=self.notify,font=("times",10,"bold"),bg="cyan")
        self.notify_button.place(x=750,y=500)
 #creating a button
        self.quit_button = tk.Button(master, text="QUIT", command=master.destroy,font=("times",15,"bold"),bg="red")
        self.quit_button.place(x=800,y=550)
#creating time delay

##########display a desktop notification on the user's system screen with the specified
    def notify(self):
        title = self.title_entry.get()
        message = self.message_entry.get()
        delay = float(self.delay_entry.get())

        notification.notify(
            title=title,
            message=message,
            timeout=60
        )

        tk.messagebox.showinfo(title="Notification Sent", 
                               message="Your notification has been sent!")


root = tk.Tk()
app = DesktopNotifier(root)
root.mainloop()





#NOTE:using libraries are PLYER & NOTIFI2

 
