nums_sam=[2,2]
target_sam=2
def searchRange(nums, target):
    found=False
    low=0
    upper=len(nums)-1
    while low<=upper and found==False:
        mid=round((low+upper)/2)
        if nums[mid]<target:
            low=mid+1
        elif nums[mid]>target:
            upper=mid-1
        elif nums[mid]==target:
            answer=mid
            found=True
    if found==False:
        answer=-1
    print(answer)
    if answer==-1:
        print([-1,-1])
    else:
        upper_point=answer
        lower_point=answer
        upper_stop=False
        lower_stop=False
        while upper_stop==False or lower_stop==False:
            print(lower_point,upper_point)
            try:
                if nums[upper_point+1]==target and upper_point<len(nums)-1:
                    upper_point=upper_point+1
                else:
                    upper_stop=True
            except:
                print("upper reach limit")
                upper_stop=True
            try:
                if nums[lower_point-1]==target and lower_point>0:
                    lower_point=lower_point-1
                else:
                    lower_stop=True
            except:
                print("lower reach limit")
                lower_stop=True
        print([lower_point,upper_point])
    return answer
    

print(searchRange(nums_sam,target_sam))