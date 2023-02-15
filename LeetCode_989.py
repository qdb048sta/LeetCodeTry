#LeetCode_989
import math
def add_together(num,k):
    num2=[int(i) for i in str(k)]
    end=False
    adv=0
    ans=[]
    while end==False:
        print("input",num,num2)
        if len(num)==0 and len(num2)==0:
            end=True
            if adv==1:
                ans.append(1)
        elif len(num)==0:
            num2_last=num2[-1]
            if num2_last+adv>=10:
                ans.append(num2_last+adv-10)
                adv=1
            else:
                ans.append(num2_last+adv)
                adv=0
            del num2[-1]
        elif len(num2)==0:
            num_last=num[-1]
            if num_last+adv>=10:
                ans.append(num_last+adv-10)
                adv=1
            else:
                ans.append(num_last+adv)
                adv=0
            del num[-1]
        else:
            num_last=num[-1]
            num2_last=num2[-1]
            if num_last+num2_last+adv>=10:
                ans.append(num_last+num2_last+adv-10)
                adv=1
            else:
                ans.append(num_last+num2_last+adv)
                adv=0
            del num[-1]
            del num2[-1]
        print(ans)
    ans.reverse()
    return ans

#print(add_together([1,2,0,0,5,2,1,3,2,5,6,2,4],3200025244))
print(add_together([1,2,6,3,0,7,1,7,1,9,5,6,6,4,4,0,0,0,6,3],516))
print(str(1263071719566440063+516))