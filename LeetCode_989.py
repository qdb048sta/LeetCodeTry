#LeetCode_989
import math
def add_together(num,k):
    ans=0
    num2=[int(i) for i in str(k)]
    for i in range(1,len(num)+1):
        ans=ans+num[-1*i]*math.pow(10,i-1)
    for i in range(1,len(num2)+1):
        ans=ans+num2[-1*i]*math.pow(10,i-1)
    return int(ans)
print(add_together([1,2,0,0,5,2,1,3,2,5,6,2,4],3200025244))