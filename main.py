import colorGui
import ioUtils
import os
import json


if "learned.json" not in os.listdir():
    ioUtils.setLearned(ioUtils.getinitLearned())
gui = colorGui.ColorGUI()