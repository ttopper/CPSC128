# write_coords.py
coords = [[12, 31], [75, 19], [28, 51]]
fname = input('Name of file to create? ')
f = open(fname, 'w')
for coord in coords:
    f.write(str(coord[0])+' '+str(coord[1])+'\n')
f.close()
