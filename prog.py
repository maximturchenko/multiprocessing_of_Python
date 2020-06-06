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


def workingProcsort(pid_n , values):
    #Сортируем подмассив `values` обычной сортировкой вставками 
    for i in range(1, len(values)):
        ito_insert = values[i]
        j = i - 1
        while j >= 0 and values[j] > ito_insert:
            values[j + 1] = values[j]
            j -= 1
        values[j + 1] = ito_insert

    #Надо записать во временный файл каждого процесса 
    cur_path = os.path.dirname(__file__)
    new_path = cur_path + '\\temp\\'+str(pid_n)+'.dat'

    with open(new_path, "wb") as file: 
        for i in range(len(values)):
            file.write(struct.pack('I', values[i]))

def mainProc():
    path = os.path.dirname(__file__)
    files = os.listdir(path+"\\temp")
    values = []
    for f in range(len(files)):
        with open("temp/"+files[f] , "rb") as file: 
            bytes = file.read() 
            values = values + list(struct.unpack('4I', bytes)) 
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    values = merge_sort(values)    
    with open("file_done.dat", "wb") as file:
        for i in range(len(values)):
            file.write(struct.pack('I', values[i]))
    print("Данные отсортированные значения записаны в файл: file_done.txt "+str(values))               

def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0    
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1
    return sorted_list

def merge_sort(nums):  
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


if __name__ == '__main__':
         
    #Параметры
    part = 16 #Всего чисел для сортировки можно взять
    filename = 'file.dat' #Всего чисел для сортировки можно взять 
    if len (sys.argv) > 1: 
        filename = sys.argv[1]
        part = sys.argv[2]

    if os.path.exists('temp'):
        shutil.rmtree('temp')
    os.mkdir("temp")

    processes = []
    with open(filename, "rb") as file: 
        i=0 
        while True:
            bytes = file.read(part)
            #print(len(bytes))
            if bytes == "" or  bytes == "b''" or len(bytes)==0:
                break
            values = struct.unpack(str(part/4)+'I', bytes) 
            process1 = Process(target = workingProcsort, args=(i , list(values)))          
            process1.start() 
            processes.append(process1)
            i+=1
    for i in range(len(processes)): 
        processes[i].join()
        print(processes[i].pid)
 
    main_process = Process(name='Main_process', target=mainProc) 
    main_process.start()
    main_process.join()
           