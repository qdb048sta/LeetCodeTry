from re import L


pushed = [1,2,3,4,5]
popped = [4,3,5,1,2]
push_point=0
popped_point=0
stack=[]
sus=True
while sus==True and popped_point<=len(popped)-1:
    pop=popped[popped_point]
    if pop not in stack:
        finished=False
        while finished==False:
            if len(pushed)>0:
                lp=pushed[0]
                stack.append(lp)
                del pushed[0]
                if lp==pop:
                    finished=True
            else:
                finished=True
    
    finished=False
    print("stack before",stack)
    print("now on",pop)
    while finished==False:
        if len(stack)==0 and finished==False:
            finished=True
            sus=False
        elif len(stack)>0:
            first=stack[-1]
            del stack[-1]
            if first==pop:
                finished=True
        print(stack)
    popped_point=popped_point+1
print( sus)
for i in [1,2,3,4,5]:
    for k in [6,7,8,9]:
        if k==7:
            break
        print(i,k)