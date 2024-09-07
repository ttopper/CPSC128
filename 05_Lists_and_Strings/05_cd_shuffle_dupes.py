# CDShuffle_dupes.py
import random
print('tracks | dupes')
print('-------+------')
for tracks in [1,2,5,10,20,50,100]:
    loops = 0
    playlist = []
    while len(playlist) < tracks:
        tracknum = random.randint(1,tracks)
        loops = loops + 1
        if tracknum not in playlist:
            playlist.append(tracknum)
    dupes = loops - tracks
    print(f"{tracks:4d}   |{dupes:5d}")
