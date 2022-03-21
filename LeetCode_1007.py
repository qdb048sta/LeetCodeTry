tops=[1,2,1,1,1,2,2,2]
bottoms=[2,1,2,2,2,2,2,2]

first=[tops[0],bottoms[0]]
rot=[bottoms[0],tops[0]]
curmin=len(tops)
print(first)
print(rot)
for i in range(0,4):
    ind=0
    contin=True
    curcont=0
    if i==0:#check top not rot
        while ind<=len(tops)-1 and contin==True:
            if tops[ind]==first[0]:
                pass
            elif tops[ind]!=first[0]:
                if bottoms[ind]==first[0]:
                    curcont=curcont+1
                else:
                    contin=False
            ind=ind+1
        if contin==True:
            if curcont<=curmin:
                curmin=curcont
            
    elif i==1:#check bot not rot
        while ind<=len(tops)-1 and contin==True:
            if bottoms[ind]==first[1]:
                pass
            elif bottoms[ind]!=first[1]:
                if tops[ind]==first[1]:
                    curcont=curcont+1
                else:
                    contin=False
            ind=ind+1
            #print(curcont,bottoms[ind],tops[ind],first[1],contin)
        if contin==True:
            if curcont<=curmin:
                curmin=curcont
    elif i==2:#check top rot
        while ind<=len(tops)-1 and contin==True:
            if tops[ind]==rot[0]:
                pass
            elif tops[ind]!=rot[0]:
                if bottoms[ind]==rot[0]:
                    curcont=curcont+1
                else:
                    contin=False
            ind=ind+1
        if contin==True:
            if curcont<=curmin:
                curmin=curcont
    elif i==3:#check bot rot
        while ind<=len(tops)-1 and contin==True:
            if bottoms[ind]==rot[1]:
                pass
            elif bottoms[ind]!=rot[1]:
                if tops[ind]==rot[1]:
                    curcont=curcont+1
                else:
                    contin=False
            ind=ind+1
        if contin==True:
            if curcont<=curmin:
                curmin=curcont
    print(curmin,contin)
if curmin<len(tops):
    print("final",curmin)
else:
    print(-1)