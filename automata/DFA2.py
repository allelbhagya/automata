# language accepting all strings starting with 'ab'


def q0(string):
    if string[0] == "a":
        return q1(string)
    elif string[0] == "b":
        return dead(string)
    else:
        not_present(string)


def q1(string):
    if string[1] == "b":
        return q2(string)
    elif string[1] == "a":
        return dead(string)
    else:
        not_present(string)


def q2(string):
    if len(string) == 2:
        return present(string)
    elif len(string) > 2:
        for i in string[1:]:
            if i != "a" and i != "b":
                not_present(string)
        else:
            return present(string)
    else:
        not_present(string)


def dead(string):
    return "dead state"


def not_present(string):
    return '"{}" is not present in the language'.format(string)


def present(string):
    return '"{}" is present in the language'.format(string)


string = input(str())
print(q0(string))
