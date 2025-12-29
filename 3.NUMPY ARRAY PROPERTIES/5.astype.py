import numpy as np
matrix1=np.array([[1.3,2.2,3],
                 [4,5,6.5],
                 [7,8,9.0]])
print(matrix1.dtype)
matrix1=matrix1.astype("int")
print(matrix1.dtype)
