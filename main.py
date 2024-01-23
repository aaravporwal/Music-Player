import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os

player = tkinter.Tk()
player.title("Music Player")
player.geometry("370x255")

var = tkinter.StringVar()
var.set("Select the song to play")

os.chdir(askdirectory())
songlist = os.listdir()

playing = tkinter.Listbox(player,font="Helvetica 16 bold",width="33",bg="black",fg="white",selectmode=tkinter.SINGLE)

for item in songlist:
    playing.insert(0,item)

pygame.init()
pygame.mixer.init()
current_song_index = 0

def play():
    global current_song_index
    pygame.mixer.music.load(playing.get(current_song_index))
    name = playing.get(current_song_index)
    var.set(f"{name[:100]}..." if len(name)>102 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

def next_song():
    global current_song_index
    current_song_index += 1
    if current_song_index >= len(songlist):
        current_song_index = 0
    playing.selection_clear(0, tkinter.END)
    playing.selection_set(current_song_index)
    play()

text = tkinter.Label(player,font="Helvetica",textvariable=var).grid(row=0,columnspan=4)
playing.grid(columnspan=4)

playB = tkinter.Button(player, width=7, height=1, font="Helvetica", text="Play", command=play, bg="lightgreen").grid(row=2,column=0)
pauseB = tkinter.Button(player, width=7, height=1, font="Helvetica", text="Pause", command=pause, bg="lightblue", fg="black").grid(row=2,column=1)
resumeB = tkinter.Button(player, width=7, height=1, font="Helvetica", text="Resume", command=resume, bg="lightpink", fg="black").grid(row=2,column=2)
nextB = tkinter.Button(player, width=7, height=1, font="Helvetica", text="Next", command=next_song, bg="lightyellow", fg="black").grid(row=2,column=3)

player.mainloop()
