#Q = ['q0','q1','q2','q3','D'] set of all states
#summation - ['a','b'] set of input symbols
#q = ['q0'] initial state
#F - ['q3'] - set of final states
#delta - transition function

def q0(string):
    if len(string)<2:
        return 'not present in language'
    if string[0] == 'a':
        return q1(string)
    elif string[0] == 'b':
        return q2(string)
    else:
        return 'not present in language'
def q1(string):
    if string[1] == 'a':
        return q3(string)
    elif string[1]=='b':
        return dead(string)
    else:
        return 'not present in language'
def q2(string):
    if string[1] == 'b':
        if len(string)>2:
            return q3(string)
        else:
            return 'string is present in the language'
    elif string[1]=='a':
        return dead(string)
    else:
        return 'not present in language'
def q3(string):
    if len(string)==2:
        return 'string is present in language'
    else:
        for i in string[2:]:
            if i!='a' or i!='b':
                return 'not present in language'
        return 'string is present in language'
def dead(string):
        return 'not present in language/dead state'

print("\nLanguage containing all the strings starting with 'aa' or 'bb' \n")
string = str(input())
print(q0(string))
