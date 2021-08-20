import sys
import itertools
import random
import numpy as np
import cv2 as cv

MAP_FILE = 'map.png'
SA1_CORNER = (130, 265, 180, 315)
SA2_CORNER = (80, 255, 130, 305)
SA3_CORNER = (105, 205, 155, 255)


class Search():

    def __init__(self, name):
        self.name = name
        self.img = cv.imread(MAP_FILE, cv.IMREAD_COLOR)
        if self.img is None:
            print('Error! Could not open map file {}'.format(MAP_FILE), file=sys.stderr)
            sys.exit(1)

        self.area_actual = 0
        self.sailor_actual = [0, 0] #local coordinates search area
        