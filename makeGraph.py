from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import ioUtils
import handleColor


def makeGraph():
    learned = ioUtils.getLearned()

    # Creating figure
    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection="3d")
    colorToMLib = {
        "RED":"red",
        "ORANGE":"darkorange",
        "YELLOW":"yellow",
        "GREEN":"green",
        "BLUE":"blue",
        "PURPLE":"purple",
        "PINK":"hotpink",
        "BROWN":"brown",
        "WHITE":"white",
        "LIGHT GRAY":"lightgray",
        "DARK GRAY":"darkgray",
        "BLACK":"black"
    }
    # Creating plot
    for l in learned:
        x = []
        y = []
        z = []
        for c in learned[l]:
            colorRgb = handleColor.colorDecompact(c[0])
            x.append(colorRgb[0])
            y.append(colorRgb[1])
            z.append(colorRgb[2])
        color = "blue"
        if l in colorToMLib:
            color = colorToMLib[l]
        ax.scatter3D(x, y, z, color=color, alpha=1)
        ax.set_xlabel('Red')
        ax.set_ylabel('Green')
        ax.set_zlabel('Blue')

    # show plot
    plt.savefig('test.png', transparent=True)
    plt.show()
