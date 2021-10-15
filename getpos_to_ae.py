### UserInput ###
setpos = "setpos 228.738983 -1478.905029 22.854500"


def toInt():
    st = setpos.split()[1:]
    ilst = [int(float(i)) for i in st]

    x = ilst[0]
    y = ilst[1]
    z = ilst[2]

    return [-y, -z, x]


if __name__ == '__main__':
    print(toInt())
