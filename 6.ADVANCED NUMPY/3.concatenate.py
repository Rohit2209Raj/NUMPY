'''
Docstring for ADVANCED NUMPY.3.concatenate
np.concatenate((arr1,arr2),axis=0)
'''
import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([4,5,3,2])
new_arr=np.concatenate((arr1,arr2),axis=0)
print(new_arr)
