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

def chooseAudioPath():
    print("Hi, may you ignore me?")

#UI
root = tk.Tk()
root.title("MP4 to MP3 Converter")
root.geometry('400x200')

#Label
labelVideoPath = tk.Label(root, text="Please choose de Path of the video:")
labelVideoPath.pack()

#Field (No enabled)
fieldVideoPath = tk.Entry(root)
fieldVideoPath.config(width=40, state=tk.DISABLED)
fieldVideoPath.pack()

#Button
buttonPath = tk.Button(root, text="Video path", command=choosePath)
buttonPath.pack()

#Label Audio
labelAudioName = tk.Label(root, text="Please write a name (Optional):")
labelAudioName.pack()

#Field (Enabled)
fieldAudioName = tk.Entry(root)
fieldAudioName.config(width=40)
fieldAudioName.pack()

#Label Audio Path
labelAudioPath = tk.Label(root, text="Please choose a Path for the audio:")
labelAudioPath.pack()

#Field Audio Path
fieldAudioPath = tk.Entry(root)
fieldAudioPath.config(width=40, state=tk.DISABLED)
fieldAudioPath.pack()

#Button Audio Path
buttonAudioPath = tk.Button(root, text="Audio Path", command=chooseAudioPath)
buttonAudioPath.pack()

#Legacy
labelLegacy = tk.Label(root, text="MP4 to MP3 Converter.")
labelLegacy.pack()

root.mainloop()