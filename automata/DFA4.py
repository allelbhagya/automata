def q0(string):
    if string[0]=='a':
        return q1(string)
    elif string[0]=='b':
        return q0(string)
    else:
        return 'not a/b'

def q1(string):
    if string[1]=='b':
        return q2(string)


def q2(string):
    if string[2]=='b':
        return qf(string)

def qf(string):
    string=string[::-1]
    if string[:3]=='bba':
        return 'string is present in language'

print(q0('abb'))