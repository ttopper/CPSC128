# CDShuffle_c.py
import random
tracks = int(input('How many tracks are on the CD? '))
SHUFFLES = 2*tracks
                   
tracklist = list(range(1, tracks+1))
playlist = []
while len(tracklist) > 0:
    track_posn = random.randint(0,len(tracklist)-1)
    playlist.append(tracklist[track_posn])
    del(tracklist[track_posn])

print(playlist)
