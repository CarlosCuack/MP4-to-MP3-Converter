import moviepy.editor as mp

# path = "C:\Users\lenoc\Documents\GitHub\MP4-to-MP3-Converter\src\video.mp4"

mp4 = mp.VideoFileClip(r"C:\Users\lenoc\Documents\GitHub\MP4-to-MP3-Converter\src\video.mp4") #Load the .mp4

mp4.audio.write_audiofile("audio.mp3")