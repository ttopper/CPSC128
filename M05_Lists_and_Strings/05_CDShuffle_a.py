# CDShuffle_a.py
import random
tracks = int(input('How many tracks are on the CD? '))
                   
playlist = []
while len(playlist) < tracks:
    tracknum = random.randint(1,tracks)
    if tracknum not in playlist:
        playlist.append(tracknum)

print(playlist)