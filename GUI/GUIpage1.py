from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry('1000x700')
root.title("The Mood Player")
root.iconbitmap(r'C:\Users\DESKTOP\Desktop\Mood_Player\GUI\music_player_Gt8_icon.ico')   #update the path according to the system

label= Label(root, text="The Mood Player")
label.pack(side='top')

canvas=Canvas(root,height=400, width=700, bg="grey", relief="raised",borderwidth=2)
o= canvas.create_oval(160,40,840,360,fill="black")
t= canvas.create_text(500,180, text="Choose the music according to mood", fill="white", font=2)
l= canvas.create_line(360,200,640,200,width=5,fill="grey")
canvas.pack(side="top",fill=BOTH)

btn1=Button(root, text="AUTO")
btn2=Button(root, text="MANUAL")
btn1.place(relx=0.48, rely=0.7, anchor="center")
btn2.place(relx=0.54, rely=0.7, anchor="center")

root.mainloop()