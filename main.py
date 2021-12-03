from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
def addsongs():
    temp_song = filedialog.askopenfilenames(initialdir="/", title="Choose a song",filetypes=(("mp3 Files", "*.mp3"),))
    for i in temp_song:
        i = i.replace(" ", "")
        songs_list.insert(END,i)

def deletesong():
    curr_song = songs_list.curselection()
    songs_list.delete(curr_song[0])

def Play():
    song = songs_list.get(ACTIVE)
    song = f'{song}'
    mixer.music.load(song)
    mixer.music.play()

def Pause():
    mixer.music.pause()

def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def Resume():
    mixer.music.unpause()

def Previous():
    previous_one = songs_list.curselection()
    previous_one = previous_one[0] - 1
    temp2 = songs_list.get(previous_one)
    temp2 = f'{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(previous_one)
    songs_list.selection_set(previous_one)


def Next():
    next_one = songs_list.curselection()
    next_one = next_one[0] + 1
    temp = songs_list.get(next_one)
    temp = f'{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    songs_list.selection_clear(0, END)
    songs_list.activate(next_one)
    songs_list.selection_set(next_one)

window=Tk()
window.title("Kushal's music player")
mixer.init()
#create the listbox to contain songs
songs_list=Listbox(window, selectmode=SINGLE, bg="dark blue", fg="red", font=('arial', 15), height=12, width=47)
songs_list.grid(columnspan=20)
#font is defined which is to be used for the button font
defined_font = font.Font(family='')
#play button
play_button=Button(window, text="▶",fg='purple', width =7, command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)
#pause button
pause_button=Button(window, text="⏸",fg='purple', width =7, command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)
#stop button
stop_button=Button(window, text="⏹",fg='purple', width =7, command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)
#resume button
Resume_button=Button(window, text="Resume",fg='purple', width =7, command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)
#previous button
previous_button=Button(window, text="⏮",fg='purple', width =7, command=Previous)
previous_button['font']=defined_font
previous_button.grid(row=1,column=4)
#nextbutton
next_button=Button(window, text="⏭",fg='purple', width =7, command=Next)
next_button['font']=defined_font
next_button.grid(row=1,column=5)
#menu
my_menu=Menu(window)
window.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Remove Song",command=deletesong)
mainloop()


