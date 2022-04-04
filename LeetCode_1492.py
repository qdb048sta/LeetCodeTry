n=189756341099642144773211556149462
fact={}
start=2
while n>1 and start<=n:
    if n%start==0:
        if start not in fact:
            fact[start]=1
        else:
            fact[start]=fact[start]+1
        n=int(n/start)
        start=2
    else:
        start=start+1
    print("now n",n,"now start",start)
print(fact)