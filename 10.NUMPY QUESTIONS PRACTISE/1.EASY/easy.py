import numpy as np
# # 1. A sensor records temperature every hour for 24 hours. 
# # Create a NumPy array of 24 values between 15 and 35 (inclusive).

# arr=np.linspace(15,35,24)
# print(arr)


# # Given an array of daily sales: 
# # [1200, 1500, 1100, 1800, 1700] 
# # o Find maximum, minimum, and average sales. 

# arr=np.array([1200, 1500, 1100, 1800, 1700])
# print(f'average: {np.mean(arr)}')
# print(f'maximum: {np.max(arr)}')
# print(f'minimum: {np.min(arr)}')


# # 3. A student has marks in 6 subjects. 
# # Create an array and: 
# # o Add 5 grace marks to each subject. 

# marks=np.array([45,67,87,33,56,78])
# arr=marks+5
# print(arr)



# # 4. You have an array of ages of people in a survey. 
# # Extract all ages greater than 18. 

# arr=np.array([34,53,23,45,33,23,21,21,12,3,4,78,56,73,21,22,1,2,2])
# print(arr[arr>18]) #acutlagy gives the arrray
# print(arr>18) #print true and false



# # 5. Create a 2×3 matrix representing sales of 2 products over 3 days. 
# # Print: 
# # o Row-wise sum 
# # o Column-wise sum
# matrix=np.array([[300,450,500],
#                  [530,130,420]])
# print(np.sum(matrix,axis=1))
# print(np.sum(matrix,axis=0))
# print(matrix.sum(axis=0))

# 6. Reverse a NumPy array without using loops.
# arr=np.array([1,2,3,4,5,6,7,8])
# arr=arr[::-1]
# print(arr)

# # 7. Given [10, 20, 30, 40, 50], replace: 
# # o values > 25 with 1 
# # o values ≤ 25 with 0
# arr=np.array([10, 20, 30, 40, 50])
# # arr[arr<=25]=0
# # arr[arr>25]=1
# arr=np.where(arr>25,1,0)
# print(arr)


# # 8. Check whether an array contains any negative values. 
# arr=np.array([10,2,3,5,-4,3])
# # print(arr[arr<0])
# print(np.any(arr<0))  #IMPORTANT AND NEW

9

# A company records daily profits for a week.
# Given an array of profits, find the total profit and the day with the highest profit.


# arr=np.array([100,134,432,342,89,678,456,234])
# print(np.sum(arr))
# print(np.max(arr))
# print(np.argmax(arr)) # returns highest day
# print(np.argmin(arr))


# 10.

# You are given heights of students in centimeters.
# Convert all heights to meters using NumPy operations.

# heights=np.array([175,165,178,159,181,193,174])
# # heights=heights.astype(float) not required
# heights_m=heights/100
# print(heights_m)

# 11.

# Given a NumPy array of test scores,
# count how many students scored above the class average.
# arr=np.array([10,20,30,40,50,60,70,80,90,100])
# print(np.mean(arr))
# # arr2=arr[arr>np.mean(arr)]
# # print(len(arr2))
# print(np.sum(arr>np.mean(arr)))

# 12.

# You have a 3×3 matrix representing marks of 3 students in 3 subjects.
# Find the average marks of each student.
# matrix=np.array([[90,80,70],
#                  [67,87,77],
#                  [59,79,99]])
# print(np.mean(matrix,axis=1))

# # 13.

# # Given an array containing some missing values (np.nan),
# # replace all missing values with the mean of the array.
# arr=np.array([10,30,50,np.nan,230])
# x=np.nanmean(arr)
# print(x)
# arr=np.nan_to_num(arr,nan=x)
# print(arr)



# 14.

# You have an array of exam scores.
# Round all scores to the nearest multiple of 5.

# arr=np.array([10,12,23,43,23,67,89,0])
# # arr=np.where((arr % 5 <=2),arr-(arr % 5),arr+(5-(arr%5)))
# arr= (np.round(arr / 5)) * 5
# print(arr)


# 15.

# # Given an array of employee salaries, increase salaries by 10% for everyone earning less than 50,000.
# arr=np.array([56000,45000,67000,34000,55000,23000])
# # arr=np.where(arr<50000,arr*1.10,arr)
# arr = np.where(arr < 50000, np.round(arr * 1.10), arr).astype(int)
# print(arr)

# 16.

# Create a 4×4 matrix of random integers between 1 and 20.
# Find the maximum value in each row and each column.
# matrix=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# matrix=np.random.randint(1,21,size=(4,4))
# print(matrix)
# print(np.max(matrix,axis=0))
# print(np.max(matrix,axis=1))


# 17.

# You have two arrays representing daily sales of two stores.
# Compute the total sales per day by adding the arrays element-wise.
# arr1=np.random.randint(1,100,10)
# arr2=np.random.randint(1,100,10)
# # print(arr1+arr2)
# # Better method
# arr_total=np.add(arr1,arr2)
# print(arr_total)

# 18.

# Given an array of ages, count how many are between 18 and 30 inclusive.
# arr=np.random.randint(1,100,40)
# print(arr)
# print(np.sum((arr>=18) & (arr<=30)))

# 19.

# # You have a 2D array of marks.
# # Find the student (row) with the highest total marks.
# matrix=np.array([[100,90,89],[98,78,88],[90,90,69]])
# # print(np.max(np.sum(matrix,axis=1)))
# arr_row_sum=np.sum(matrix,axis=1)
# print(np.argmax(arr_row_sum)) 


# 20.

# Create an array of 15 random integers.
# Sort the array without changing the original array.
# arr=np.random.randint(1,100,15)
# arr2=np.sort(arr)
# print(arr2)

# 21.

# You have an array representing daily temperatures.
# Convert all temperatures from Celsius to Fahrenheit.

# celsius=np.array([32,34,45,21,12])
# # fahrenheit=((celsius*(9/5))+32).astype(int)
# fahrenheit = np.round((celsius * (9/5)) + 32).astype(int)
# print(fahrenheit)
# # 22.

# Given a 1D array, reshape it into a 2D array with 3 columns (number of rows should adjust automatically).
# arr=np.array([1,2,3,4,5,6,7,8,9])
# arr=np.array([1,2,3,4,5,6])
# matrix=arr.reshape(-1,3)
# print(matrix)

# 23.

# You have an array with repeated values.
# Find all unique values and their counts.
# arr=np.array([1,1,2,3,4,5,5,5,6,7,8])
# # arr2=np.unique(arr)
# arr2,count=np.unique(arr,return_counts=True)
# print(arr2,count)