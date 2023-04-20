import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

#Variables


#Script
def choosePath():
    print("HI")

def convertVideo():
    path = r"C:\Users\lenoc\Documents\GitHub\MP4-to-MP3-Converter\src\video.mp4"

    mp4 = mp.VideoFileClip(path) #Load the .mp4

    mp4.audio.write_audiofile("audio.mp3")

#UI


