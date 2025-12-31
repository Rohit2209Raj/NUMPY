'''
Docstring for 5.RESHAPING AND MANIPULATION.2.flatten_revel
.flatten()->copy
.ravel()->view
'''



import numpy as np
arr=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]],
            )
print(arr.ravel())
print(arr.flatten())


