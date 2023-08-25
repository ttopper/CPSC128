
TESTS = ['madam', 'maam', 'motor', 'moor', 'a', 'oo', 'at',
         'A man, a plan, a canal, Panama!']
print('Testing Solution 1:')
for s in TESTS:
    print(s,end='')
    # Preprocess s to lower case and remove non-alphas.
    s_new = ''
    for c in s:
        if c.isalpha():
            if c.isupper():
                s_new = s_new + c.lower()
            else:
                s_new = s_new + c
    s = s_new # Replace s with s_new.
    
    # Test to see if s is a palindrome using Solution 1.
    palindrome = True
    for offset in range(0, len(s)//2):
        if s[offset] != s[len(s)-1-offset]:
           palindrome = False
    if palindrome:
        print("is a palindrome!")
    else:
        print("is NOT a palindrome.")

'''
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
    print("{:4d}   |{:5d}".format(tracks, dupes))


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


# CDShuffle_a.py
import random
tracks = int(input('How many tracks are on the CD? '))
                   
playlist = []
while len(playlist) < tracks:
    tracknum = random.randint(1,tracks)
    if tracknum not in playlist:
        playlist.append(tracknum)

print(playlist)
'''