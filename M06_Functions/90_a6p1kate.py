def ndigits(num):
    str_num = str(num)
    if str_num[0] == '-':
        str_num = str_num[1:]
    return len(str_num)

def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def ispos(num):
    if num > 0:
        return True
    else:
        return False

def line(num,char):
    print(num*char)
    return None

line(60, '=')
print('Function practice')
line(60, '-')
num = int(input('Give me an integer value: '))
print('Your number contains', ndigits(num), end = ' ')
print('digits, is', even_or_odd(num), end = '')
if ispos(num):
    print(', and is positive.')
else:
    print(', but is not positive.')
line(60, '-')

