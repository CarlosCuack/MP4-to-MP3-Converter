import moviepy.editor as mp

path = "video.mp4" #Temporal

mp4 = mp.VideoFileClip(path) #Load the .mp4

mp4.audio.write_audiofile("audio.mp3")