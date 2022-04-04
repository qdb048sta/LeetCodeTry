def searchMatrix(matrix, target):
    tail_start=0
    tail_end=len(matrix)
    lf=False
    while tail_end>=tail_start and lf==False :
        mid_end=(tail_start+tail_end)//2
        if matrix[mid_end][-1]>=target:
            lf=True
        elif matrix[mid_end][-1]<target:
            tail_start=mid_end
    head_start=tail_start
    head_end=tail_end
    hf=False
    while head_end>=head_start and hf==False:
        mid_head=(head_start+head_end)//2
        if matrix[mid_head][0]<=target:
            hf=True
        elif matrix[mid_head][0]>target:
            head_end=mid_head
    print(hf,lf,tail_start,tail_end,head_start,head_end)
    if lf==True and hf==True:
        target_row=matrix[head_end]
        start=0
        found=False
        end=len(target_row)
        print(target_row)
        while end>=start and found==False:
            mid=(start+end)//2
            if target_row[mid]==target:
                found=True
            elif target_row[mid]>target:
                end=mid
            elif target_row[mid]<target:
                start=mid
        return found
    else:
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
#searchMatrix(matrix1,target1)
for i in range(0,len(matrix)):
    if matrix[i][-1]>=target:
        end=i
        break
for i in range(end,len(matrix)):
    if matrix[i][0]<=target:
        start=i
        break
if start==end:
    left=0
    right=len(matrix[start])-1
    found=False
    print(matrix[start])
    while left <= right and found==False:
        mid = left + (right - left) // 2
        #print(left,right)
        print(mid)
        if matrix[start][mid] == target:
            found=True
        elif matrix[start][mid] < target:
            left = mid 
        elif matrix[start][mid] > target:
            right = mid
    print(found)
        
else:
    print( False)