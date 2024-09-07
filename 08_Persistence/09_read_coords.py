# read_coords.py
coords = []
fname = input('Name of file to read from? ')
f = open(fname, 'r')
for line in f:
    (x_string, y_string) = line.split()
    coords.append([int(x_string),int(y_string)])
f.close()
print('coords =', coords)
