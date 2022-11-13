# language containing strings starting with a and ending with b


def q0(string):
    if string[0] == "a":
        return q1(string)
    elif string[0] == "b":
        return dead(string)
    else:
        not_present(string)


def q1(string):
    if len(string) == 2:
        return q2(string)
    elif len(string) > 2:
        for i in string[2:-1]:
            if i != "a" and i != "b":
                not_present(string)
        return q2(string)
    else:
        not_present(string)


def q2(string):
    if string[-1] == "b":
        return present(string)
    else:
        not_present(string)


def dead(string):
    return "dead state/not present in the language"


def not_present(string):
    return '"{}" is not present in the language'.format(string)


def present(string):
    return '"{}" is present in the language'.format(string)


string = input()
print(q0(string))
