import numpy as np
# 17. A dataset contains NaN values in salary data. 
# • Replace missing salaries with mean salary.

# arr=np.array([12000,14500,np.nan,7500,5600,23000,np.nan])
# meanarr=np.nanmean(arr)
# arr[np.isnan(arr)] = meanarr
# # arr=np.nan_to_num(arr,nan=meanarr)
# print(arr)


# # 18. Given a dataset of product ratings (1–5): 
# # • Find most frequent rating 
# # • Find standard deviation 
# arr=np.array([1,4,5,3,2,4,4,3,4,2,4])
# print(np.std(arr))
# unique_vals, counts = np.unique(arr, return_counts=True)
# # print(unique_vals)
# # print(counts)
# print(unique_vals[np.argmax(counts)])


# 19. Detect outliers in an array using: 
# • mean ± 2 × std deviation 

# arr=np.array([1,4,5,3,2,4,4,3,4,2,4])
# meanarr=arr.mean()
# stdarr=arr.std()
# print(( (arr > (meanarr + 2*(stdarr))) |
#                (arr < (meanarr - 2*(stdarr))) ))



# 20. You have rainfall data for 12 months: 
# • Identify dry months (rainfall < 50) 
# • Count them 
# arr=np.array([100,25,48,69,89,56,23,78,98,98,58,12])
# print(np.sum(arr<50))
# print(np.where(arr<50)[0]) # iportant


# 21. Given marks of students: 
# • Assign grades: 
# o ≥90 → A 
# o ≥75 → B 
# o ≥60 → C 
# o else → D 
# (Use NumPy only, no loops)

marks=np.array([100,45,67,34,89,67,56,87,34,78,98])
# grades=np.where(marks>= 90,'A',
#                 np.where(marks>= 75,'B',
#                     np.where(marks>= 60,'C','D')
#                     )
#                 )
# print(grades) 

# conditions=[
#     marks>=90,
#     marks>=75,
#     marks>=60,
# ]
# grades= ['A','B','C']
# print(np.select(conditions,grades,default='D'))

        

        

# 22. Compare two exam result arrays and find: 
# • how many students improved 
# • how many declined

arr1=np.array([100,56,78,49,87,67])
arr2=np.array([98,56,78,45,67,34])
print(np.sum(arr1<arr2))
print(np.sum(arr1>arr2) )

# 23. Given stock prices of 100 days: 
# • Compute daily returns (%)