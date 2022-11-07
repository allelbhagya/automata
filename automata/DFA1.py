states = ['q0','q1','q2','q3','D']
def q0(string):
    if len(string)<2:
        return 'not present in language'
    if string[0] == 'a':
        return q1(string)
    elif string[0] == 'b':
        return q2(string)
def q1(string):
    if string[1] == 'a':
        if len(string)>2:
            return q3(string)
        else:
            return 'string is present in the language'
    elif string[1]=='b':
        return dead(string)
    else:
        return 'not in language'
def q2(string):
    if string[1] == 'b':
        if len(string)>2:
            return q3(string)
        else:
            return 'string is present in the language'
    elif string[1]=='a':
        return dead(string)
    else:
        return 'not in language'
def q3(string):
    if string[2]=='a' or string[2]=='b':
        return 'string is present in language'
    else:
        return 'not in language'
def dead(string):
    if len(string)==2:
        return 'string is ??'
    else:
        return 'not present in language/dead state'
print("\nLanguage containing all the strings starting with 'aa' or 'bb' \n")
x = str(input())
print(q0(x))
