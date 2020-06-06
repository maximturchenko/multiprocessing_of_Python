from __future__ import division
import random
import argparse
import struct

import math

import os
import subprocess
import sys

#Заполнение файла числами
def createourfile():
    parser = argparse.ArgumentParser()
    parser.add_argument('-size',action="store", dest="size", default=320, type=int)
    namespace = parser.parse_args()
    percent = int(namespace.size/100)

    with open("file.dat", "wb") as file:
        for i in range(namespace.size):
            b = random.randint(0, 4294967295)
            file.write(struct.pack('I', b))
            if i % percent == 0 or i % 1000000 == 0:
                print(str(i/percent))


if __name__ == '__main__':
  #  createourfile()
  
    #Параметры
    all = 320 #всего чисел в файле
    part = 15 #Всего чисел для вортировке можно взять
    n = math.ceil(all / part) #Считаем сколько процессов запустить 
    
    #
    n=5
    pipes = []
    for i in range(n):
        command = [sys.executable, child]
        pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
        pipes.append(pipe)
    #

    with open("file.dat", "rb") as file:  
            bytes = file.read()
            values = struct.unpack('320I', bytes)

