"""This is a python program which imports data from a all_elements.txt file and finds the required elements ie. same as the ones in subset_elements.txt and append it into a new list.
This task was optimised by different functions and the time taken by each task is displayed after it completes the running process.
The numpyfunc() as the name indicates use numpy to speed up the process and datastructuremethod() uses the tuple datastructure to make things faster.
and the givenfunc() is the one with the slowest speed
This needs the import of various modules like time to measure time taken, numpy to introduce numpy array, and pandas to handle the data"""
import time
import pandas as pd
import numpy as np
#opening the text file in python and arrangement as well as storing it to a variable
with open('subset_elemets.txt') as f:
    subset_elements = f.read().split('\n')
with open('all_elements.txt') as f:
    all_elements = f.read().split('\n')
#definition of the numpyfunc() function
def numpyfunc():
    start = time.time()
    verified_elements = []
    array_sub = np.array(subset_elements)
    array_all = np.array(all_elements)

    for element in array_sub:
        if element in array_all:
            verified_elements.append(element)
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))
#definition of the datastructuremethod function
def datastructuremethod():
    start = time.time()
    verified_elements = []
    tuple_sub = tuple(subset_elements)
    tuple_all = tuple(all_elements)
    verified_elements = set(tuple_all) & set(tuple_sub)
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))
#definition of the givenfunc function
def givenfunc():
    start = time.time()
    verified_elements = []
    for element in subset_elements:
        if element in all_elements:
            verified_elements.append(element)
    print(len(verified_elements))
    print('Duration: {} seconds'.format(time.time() - start))

# the main function of the file
numpyfunc()
datastructuremethod()
givenfunc()
