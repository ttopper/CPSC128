# WordFrequencies.py
# Get the string:
test_string = '''The programmer, who needs clarity, who must talk all day to
    a machine that demands declarations, hunkers down into a low-grade annoyance.
    It is here that the stereotype of the programmer,
    sitting in a dim room, growling from behind Coke cans, has its origins.
    The disorder of the desk, the floor; the yellow Post-It notes everywhere;
    the whiteboards covered with scrawl:
    all this is the outward manifestation of the messiness of human thought.
    The messiness cannot go into the program;
    it piles up around the programmer.
    ~ Ellen Ullman
'''

# Break the string into a list of words:
words = test_string.split()
# Initialize a dictionary of counters:
word_counts = {}

# Loop through the list of words:
for word in words:
    w = word.lower()
    w = w.strip('.,;:\'"?!()') # Notice the \ to escape the ' inside the string
    if w.isalpha():
        if w in word_counts:
            word_counts[w] = word_counts[w] + 1
        else:
            word_counts[w] = 1

# Loop through the entries in the dictionary:
for word in word_counts:
    # Display the key value pair:
    print(word, ':', word_counts[word])
