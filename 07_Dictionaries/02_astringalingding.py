# astringalingding.py
test_str ='astringalingding'
counters = 26*[0] # Initialize list of counters to be 26 0s.
for ch in test_str:
    # Calculate index of counter for this letter in counters.
    index = ord(ch) - ord('a')
    # Increment appropriate counter.
    counters[index] = counters[index] + 1
for index in range(26):
    # Display letter corresponding to this index and its count.
    print(chr(ord('a')+index), counters[index])
