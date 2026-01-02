'''
Docstring for ADVANCED NUMPY.1.insert
np.insert(arr,idx,value,axis=0,1,none(optional))
insert in 2d
npinsert(matrix,idx,[list],axis=0)
'''




import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
new_arr=np.insert(arr,3,199,axis=0)
print(new_arr)
print()

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
new_matrix=np.insert(matrix,2,[100,100,100],axis=1)
print(new_matrix)

