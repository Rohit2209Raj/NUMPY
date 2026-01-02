import numpy as np
arr=np.array([10,20,np.nan,30,40,np.nan])
arr_cleaned=np.nan_to_num(arr,nan=100) #default=0
print(arr_cleaned)