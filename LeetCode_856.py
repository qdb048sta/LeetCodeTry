s="(()(()))"
stack=[]
score=0
import math
cur=0
temp=0
times=0
for k in s:
    if k=="(":
        stack.append(k)
        cur=cur+1
        if times>0:
            temp=temp+math.pow(2,times-1)
    elif k==")":
        times=cur
        cur=0
        del stack[-1]
        if len(stack)==0:
            score=score+temp*2
            times=0
            temp=0
            cur=0
    print(cur,temp,times)
print("final",score )