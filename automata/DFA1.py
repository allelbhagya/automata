# strings starting with aa and bb


states = ["q0", "q1", "q2", "q3", "dead"]


def q0(string):
    if len(string) < 2:
        return not_present(string)
    if string[0] == "a":
        return q1(string)
    elif string[0] == "b":
        return q2(string)
    else:
        return not_present(string)


def q1(string):
    if string[1] == "a":
        return q3(string)
    elif string[1] == "b":
        return dead(string)
    else:
        return not_present(string)


def q2(string):
    if string[1] == "b":
        if len(string) > 2:
            return q3(string)
        else:
            return not_present(string)
    elif string[1] == "a":
        return dead(string)
    else:
        return not_present(string)


def q3(string):
    if len(string) == 2:
        return present(string)
    else:
        for i in string[2:]:
            if i != "a" and i != "b":
                return not_present(string)
        return present(string)


def dead(string):
    return "dead state"


def not_present(string):
    return '"{}" is not present in the language'.format(string)


def present(string):
    return '"{}" is present in the language'.format(string)


print("\nLanguage containing all the strings starting with 'aa' or 'bb' \n")
x = str(input())
print(q0(x))
