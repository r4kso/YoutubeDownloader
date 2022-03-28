# !/usr/bin/env python3
# coding: utf-8
#----------------------------------------------------------------------------
# Created By : R4kso (@notaboutfran on Twitter)
# Created Date: 22/03/2022
# version = '0.1'
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

# Interfaz
root = Tk()                                     # Used to initialize Tkinter and show window
root.geometry('500x300')                        # Set windows size
root.resizable(0, 0)                            # Set the fix size of the window
root.title("Youtube Downloader")                # Used to give the title of the window

Label(root, text="Youtube Video Downloader", font = "arial 18 bold underline").pack() # Used to display text that users cannot modify

link = StringVar()                              # Stores the youtube link entered by the user

Label(root, text = 'Paste the Youtube link here: ', font = 'arial 15 bold').place(x = 120, y = 60)
link_enter = Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)     # Allows to enter the link

def videoDownloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download('Downloads/Videos')
    Label(root, text = "DOWNLOADED", font = "arial 15").place(x = 350, y = 150)

def audioDownloader():
    url = YouTube(str(link.get()))
    video = url.streams.filter(only_audio=True).first()
    out_file = video.download('Downloads/Music')
    # Save the file on mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    Label(root, text = "DOWNLOADED", font = "arial 15").place(x = 350, y = 200)

Button(root, text = "DOWNLOAD VIDEO", font = "arial 15 bold", bg = "pale violet red", padx = 2, command = videoDownloader).place(x = 140, y = 150)
Button(root, text = "DOWNLOAD AUDIO", font = "arial 15 bold", bg = "pale violet red", padx = 2, command = audioDownloader).place(x = 140, y = 200)

Label(root, text = "Created by r4kso", font = "times 12 italic bold",).place(x = 190, y = 270)



root.mainloop()