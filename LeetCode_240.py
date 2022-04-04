matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=20
start=0
end=len(matrix)
for i in range(1,len(matrix)):
    if matrix[-1*i][-1]>=target:
        end=i
        break
for i in range(0,len(matrix)):
    if matrix[i][0]<=target:
        start=i
        break
#print(matrix[start:end+1])
for k in range(start,end+1):
    left=0
    right=len(matrix[k])
    found=False
    print(matrix[k])
    while left <= right and found==False:
        print(matrix[k][left:right])
        mid = left + (right-left) // 2
        if matrix[k][mid] == target:
            found=True
            break
        elif matrix[k][mid] < target:
            left = mid+1
        elif matrix[k][mid] > target:
            right = mid-1
        print(left,right)
    if found==True:
        break
print(found)
