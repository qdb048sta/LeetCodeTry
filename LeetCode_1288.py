intervals=[[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]
intervals=[[66672,75156],[59890,65654],[92950,95965],[9103,31953],[54869,69855],[33272,92693],[52631,65356],[43332,89722],[4218,57729],[20993,92876]]
result={}
counter=0
for i in intervals:
    found=False
    ava=[]
    for k in result:
        if result[k][0][0]<=i[0] and result[k][0][1]>=i[1]:
            result[k].append(i)
            found=True
        elif result[k][0][0]>=i[0] and result[k][0][1]<=i[1]:
            ava.append(k)
    if found==False:
        result[counter]=[i]
    for a in ava:
        result[counter]=result[counter]+result[a]
        del result[a]
    if found==False:
        counter=counter+1
    print(result)
print(result)
print(len(result))
