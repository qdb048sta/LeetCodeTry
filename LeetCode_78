import itertools
nums=[1,2,4,5,7,8]
result=[]
def subset(nums):
    for i in range(0,len(nums)):
        indicator=[]
        for k in range(0,i):
            indicator.append(k)
        print(indicator)
print(subset(nums))
#what is left is the how we gonna to increment 0,1,2,3 in 0,1,2,3,4,5,6,7,8,9
def powerset(s):
    result=[]
    x = len(s)
    for i in range(1 << x):
        result.append([s[j] for j in range(x) if (i & (1 << j))])
    return(result)
