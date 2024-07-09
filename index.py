from tkinter import*
from PIL import Image,ImageTk
import time
from pygame import mixer
import pygame



w=Tk()
w.title("World of Tank")
w.geometry("1920x1080")

def fun():
    bullet_Sound = mixer.Sound('Tank_fire.wav')
    bullet_Sound.play()
    time.sleep(2.5)

    w.destroy()
    import shoot_game

  



i=Image.open("after.jpg")
im=ImageTk.PhotoImage(i)
im_lable=Label(w,image=im)
im_lable.place(x=0,y=0)
#music
pygame.init()


mixer.music.load('World_of_Tanks.wav')
mixer.music.play(-1)

my_button=Button(w,text="CLICK TO START  >> ",font=("times",30,"bold"),bd=0,command=fun,bg="#564243",fg="#c6c2c0")
my_button.place(x=1455,y=900)

w.mainloop()