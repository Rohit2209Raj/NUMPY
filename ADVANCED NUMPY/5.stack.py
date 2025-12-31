import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([4,5,3,2])
new_arr=np.vstack((arr1,arr2))
print(new_arr)
print()
new_arrh=np.hstack((arr1,arr2))
print(new_arrh)