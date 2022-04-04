m=4
array=[1,4,7,19,50,76,88,92]
index=[]
for i in range(0,m-1):
     index.append(i)
final=[]
for i in range(1,m):
    final.append(len(array)-i)
final.reverse()
print("first",index)
print("final",final)
result=[]
while index!=final:
    index[-1]=index[-1]+1
    for k in range(1,len(index)):
        if index[k*-1]>final[-1]:
            index[(k+1)*-1]=index[(k+1)*-1]+1
            index[k*-1]=index[k*-1]-final[-1]
    print(index)
    result.append(index)
    #print(result)
print(result)
