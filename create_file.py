from __future__ import division
import random
import argparse
import struct

import math

from multiprocessing import Process
import time

import sys 
import os
import shutil

#Заполнение файла числами
def createourfile(size=320):
    parser = argparse.ArgumentParser()
    parser.add_argument('-size',action="store", dest="size", default=size, type=int)
    namespace = parser.parse_args()
    percent = int(namespace.size/100)

    with open("file.dat", "wb") as file:
        for i in range(namespace.size):
            b = random.randint(0, 4294967295)
            file.write(struct.pack('I', b))
            if i % percent == 0 or i % 1000000 == 0:
                print(str(i/percent))


if __name__ == '__main__': 
    size = 320
    if len (sys.argv) > 1: 
        size = sys.argv[1]

    if not os.path.exists("file.dat"):
        createourfile(size)