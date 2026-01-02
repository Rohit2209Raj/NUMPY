'''
Docstring for ADVANCED NUMPY.6.split
np.split(arr,number of parts)
np.hsplit()
np.vsplit()
'''
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([[1,2,3,4],[5,6,7,8]])
arr_new=np.hsplit(arr1,2)
print(arr_new)
arr_new2=np.vsplit(arr2,2)
print(arr_new2)