import numpy as np
arr1=np.array([1,2,3,4]) #shape-(4,)
# when oned it giv shapes as number of columns
print(arr1.shape)
arr2=np.array([[1,2,3,4],[5,6,7,8]]) # shapre-(2,4)
result=arr1+arr2
print(result)