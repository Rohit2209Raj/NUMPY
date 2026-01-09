import pandas as pd
import numpy as np
# # 9. A company stores monthly profits for 3 years in a 1D array (36 values). 
# # Extract profits of: 
# # o Year 2 only 
# # o Last 6 months 
# profit=np.random.randint(0,100,36)
# print(profit)
# profit_2yrs=profit[0:24:1]
# profit_6months_last=profit[-6::1]
# profit_year2=profit[12:24:1]
# print(profit_year2)
# print(profit_2yrs)
# print(profit_6months_last)

# 10. Given a 5×5 matrix of employee performance scores: 
# • Extract the middle 3×3 sub-matrix 

# matrix=np.random.randint(1,100,(5,5))
# print(matrix)
# matrix_3=matrix[1:4:1,1:4:1]
# print(matrix_3)



# 11. Normalize an array of exam scores to range 0–1 using NumPy. 
# arr=np.random.randint(1,100,10)
# print(arr)
# arr=arr/np.max(arr)
# print(arr)
# arr[np.argmin(arr)]=0
# print(arr)
'''
very wrong approach
forcing min to become zero distorts relative order 
x' = x-min/(max-min)
'''
# arr=np.random.randint(1,100,10)
# print(arr)
# arr=(arr-arr.min())/(arr.max()-arr.min())
# print(arr)

# # 12. Given two arrays: 
# # • product prices 
# # • discount percentages 
# Compute final prices using broadcasting. 

# prices=np.array([100,200,300,400,500])
# discount=np.array([10,12,13,14,15])
# final=prices-((prices*discount)/100)
# print(final)


# # 13. Replace all odd numbers in an array with -1. 
# arr=np.array([19,100,2,3,4,53,24,98])
# arr=np.where(arr % 2 !=0,-1,arr)
# print(arr)

# # 14. Convert a 1D array of 12 values into: 
# # • 3×4 matrix 
# # • 4×3 matrix 
# arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# matrix_34=np.reshape(arr,(3,4))
# print(matrix_34)
# matrix_43=np.reshape(arr,(4,3))
# print(matrix_43)
# 15. Count how many values in an array are: 
# • above mean 
# • below mean 
# arr=np.array([10,20,30,40,50])
# print(np.sum(arr>np.mean(arr)))
# print(np.sum(arr<np.mean(arr)))
# 16. Given daily step counts of 30 days: 
# • Find the longest streak of days with steps > 8000.
# arr=np.random.randint(5000,10000,30)
# print(np.(arr))
# use loops