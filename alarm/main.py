from tkinter import *
from datetime import datetime

# I created the window
from xml.etree.ElementTree import tostring

root = Tk()
root.title("Calculator")
root.geometry("450x450")
icon = PhotoImage(file='alarm_logo.png')
root.iconphoto(True, icon)

#
now = datetime.now()
while now != '2022-04-28 10:05:38':
    now = datetime.now()
    print(now)

root.mainloop()
