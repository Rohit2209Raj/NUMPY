import numpy as np
arr1=np.array([1,2,3,4])

new_arr=np.delete(arr1,1)
print(new_arr)

matrix=np.array([[1,2,3],[4,5,6],[7,8,9]])
new_mat=np.delete(matrix,0,axis=0)
print(new_mat)