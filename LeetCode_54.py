matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result=[]
vert=1
count=0
while matrix!=[[]]:
    if vert%4==1:
        try:
            result.append(matrix[0][0])
            del matrix[0][0]
        except:
            del matrix[0]
            vert=vert+1


    elif vert%4==2:
        try:
            result.append(matrix[count][-1])
            del matrix[count][-1]
            count=count+1

        except:
            vert=vert+1
            count=0


        
    elif vert%4==3:
        try:
            result.append(matrix[-1][-1])
            del matrix[-1][-1]

        except:
            del matrix[-1]
            vert=vert+1


        
    elif vert%4==0:
        try:
            result.append(matrix[-1*count][0])
            del matrix[-1*count]
            count=count+1
        except:
            vert=vert+1
            count=0
    print(vert)
    print(result)
    print(matrix)
            

        
