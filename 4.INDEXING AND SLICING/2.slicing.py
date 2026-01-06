'''
Docstring for 4.INDEXING AND SLICING.2.slicing
[start:stop:step] start->stop-1
array[row_start : row_end , col_start : col_end]
array[::2,::2]
'''
import numpy as np
arr=np.array([10,20,30,40,50])
matrix=np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])
print(arr[0:3])
print(arr[-2:-5:-1])
print()
print(matrix[0:2:1,::2]) # note the difference 