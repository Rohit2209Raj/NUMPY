import numpy as np
arr=np.array([10,20,np.inf,30,40,-np.inf])
print(np.isinf(arr))
arr_cleaned=np.nan_to_num(arr,posinf=10000,neginf=-1000) #default=0
print(arr_cleaned)