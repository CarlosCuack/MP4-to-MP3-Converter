import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

#Variables
Path_Video = None

#Script
def choosePath():
    global videoPath 
    videoPath = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4")])
    Path_Video = videoPath

    fieldVideoPath.config(state=tk.NORMAL)
    fieldVideoPath.insert(0, Path_Video)
    fieldVideoPath.config(state=tk.DISABLED)

def convertVideo():
    #Raw String
    path = r"{}".format(videoPath)

    print(path)

    #Audio Name
    audioPath = videoPath.replace('.mp4', '.mp3')

    mp4 = mp.VideoFileClip(path) #Load the .mp4

    mp4.audio.write_audiofile(audioPath)

def chooseAudioPath():
    print("Hi, may you ignore me?")

#UI
root = tk.Tk()
root.title("MP4 to MP3 Converter")
root.geometry('400x110')

#Label
labelVideoPath = tk.Label(root, text="Please choose de Path of the video:")

#Field (No enabled)
fieldVideoPath = tk.Entry(root)
fieldVideoPath.config(width=40, state=tk.DISABLED)

#Button
buttonPath = tk.Button(root, text="Video path", command=choosePath)

#Label Audio
labelAudioName = tk.Label(root, text="Please write a name (Optional):")

#Field (Enabled)
fieldAudioName = tk.Entry(root)
fieldAudioName.config(width=40)

#Label Audio Path
labelAudioPath = tk.Label(root, text="Please choose a Path for the audio:")

#Field Audio Path
fieldAudioPath = tk.Entry(root)
fieldAudioPath.config(width=40, state=tk.DISABLED)

#Button Audio Path
buttonAudioPath = tk.Button(root, text="Audio Path", command=chooseAudioPath)

buttonDownload = tk.Button(root, text="Convert!!", command=convertVideo)

#Legacy
labelLegacy = tk.Label(root, text="MP4 to MP3 Converter.")

#Add
labelVideoPath.pack()
fieldVideoPath.pack()
buttonPath.pack()

# labelAudioPath.pack()
# fieldAudioPath.pack()
# buttonAudioPath.pack()

# labelAudioName.pack()
# fieldAudioName.pack()

buttonDownload.pack()
labelLegacy.pack()

#Loop
root.mainloop()