from random import randint
import json
import ioUtils

colorTTL = 1000
currentColor = None


def requestColor():
    currentColor = createColor()
    return currentColor


def createColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return [r, g, b]


def colorCompact(RGB):
    color = RGB[0]
    color = color << 8
    color += RGB[1]
    color = color << 8
    color += RGB[2]
    return color


def colorDecompact(compacted):
    color = [compacted % 256]
    compacted = compacted >> 8
    color.append(compacted % 256)
    compacted = compacted >> 8
    color.append(compacted)
    return color[::-1]


def colorToText(color):
    return "#" + ''.join("{:02X}".format(a) for a in color)



def learnColor(color, RGB):
    print(color, RGB)
    ioUtils.decTTLs()
    learned = ioUtils.getLearned()
    learned[color].append([colorCompact(RGB), colorTTL])
    ioUtils.setLearned(learned)
