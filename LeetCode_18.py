nums=[1,0,-1,0,-2,2]
result=[]
target=0
nums.sort()
print(nums)
for t1 in range(0,len(nums)):
    for t2 in range(t1+1,len(nums)):
        for t3 in range(t2+1,len(nums)):
            sub_target=target-nums[t1]-nums[t2]-nums[t3]
            if sub_target in nums[t3+1:]:
                print(nums[t3+1:])
                print(nums[t1],nums[t2],nums[t3],sub_target)
                if [nums[t1],nums[t2],nums[t3],sub_target] not in result:
                    result.append([nums[t1],nums[t2],nums[t3],sub_target])
print(result)
                