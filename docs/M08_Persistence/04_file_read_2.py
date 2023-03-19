# file_read_2.py
f = open('text_file.txt', 'r')
s = f.read()
print('s is', len(s), 'characters long.')
print(s)
f.close()