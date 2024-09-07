# ListOfDicts.py
data = [ {'id':4721, 'sex':'F', 'age':31},
         {'id':1828, 'sex':'M', 'age':56},
         {'id':7816, 'sex':'M', 'age':72},
         #. . . lots more records . . .
         {'id':3286, 'sex':'M', 'age':29},
         {'id':5063, 'sex':'F', 'age':22}
       ]

nmales = 0
nfemales = 0
for entry in data:
    if entry['sex'] == 'M':
        nmales = nmales + 1
    elif entry['sex'] == 'F':
        nfemales = nfemales + 1
print('There are', nmales, 'males and', nfemales, 'females.')

oldest = data[0]
for entry in data[1:]:
    if entry['age'] > oldest['age']:
        oldest = entry
print('The oldest person is:', oldest)
