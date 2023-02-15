#LeetCode67 
def add_two(a,b):
    check=False
    answer=""
    adv=0
    list_a=[k for k in a]
    list_b=[k for k in b]
    while check==False:
        print(list_a,list_b)
        if len(list_a)==0 and len(list_b)==0:
            if adv==1:
                answer=answer+"1"
            check=True
        elif len(list_a)==0:
            ans=str(int(list_b[-1])+adv)
            del list_b[-1]
        elif len(list_b)==0:
            ans=str(int(list_a[-1])+adv)
            del list_a[-1]
        else:
            ans_a=int(list_a[-1])
            ans_b=int(list_b[-1])
            ans=ans_a+ans_b+adv
            del list_a[-1]
            del list_b[-1]
        if ans==2:
            adv=1
            answer=answer+"0"
        else:
            adv=0
            answer=answer+str(ans)
        print("ans",ans,"adv",adv,"answer",answer)
    return answer[::-1]
print(add_two("1010","10110"))
