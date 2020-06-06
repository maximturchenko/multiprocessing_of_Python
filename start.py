from __future__ import division
import random
import argparse
import struct

import math

from multiprocessing import Process
import time

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
    all5 = 320 #всего чисел в файле
    part = 16 #Всего чисел для сортировки можно взять
    #n = math.ceil(all / part) #Считаем сколько процессов запустить 
    
    #
   # n=5
   # pipes = []
   # for i in range(n):
   #     command = [sys.executable, child]
   #     pipe = subprocess.Popen(command, stdin=subprocess.PIPE)
   #     pipes.append(pipe)
    #


    with open("file.dat", "rb") as file:  
        while True:
            bytes = file.read(part)
            #print(len(bytes))
            if bytes == "" or  bytes == "b''" or len(bytes)==0:
                break
            values = struct.unpack('4I', bytes)
               
           