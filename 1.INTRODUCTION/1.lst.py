temperatures=[32.4,37.56,33.45,31.89,45.67]
sum=0
for temp in temperatures:
    sum+=temp
print(f"The avg temperature is ",(sum/len(temperatures)))
