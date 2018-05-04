def getColor(z):
    r = 0
    g = 0
    b = 0
    if z < 255:
        r = 255
        g = z
        b = 0
    elif z < 510:
        r = 510 - z
        g = 255
        b = 0
    elif z < 765:
        r = 0
        g = 255
        b = z - 510
    elif z < 1020:
        r = 0
        g = 1020 - z
        b = 255
    elif z < 1275:
        r = z - 1020
        g = 0
        b = 255
    else:
        r = 255
        g = 0
        b = 1530 - z

    return (r, g, b)