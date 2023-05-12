# CDShuffle_b.py
import random
tracks = int(input('How many tracks are on the CD? '))
SHUFFLES = 2*tracks
                   
playlist = list(range(1, tracks+1))
for shuffle in range(SHUFFLES):
    track_posn = random.randint(0,tracks-1)
    playlist.append(playlist[track_posn])
    del(playlist[track_posn])

print(playlist)
