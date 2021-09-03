lis=list(map(int,input().split()))
a=int(input())
pair=[]
for i in range(len(lis)):
    for j in range(i+1,len(lis)):
        if lis[i]+lis[j]==a:
            pair.append(lis[i])
            pair.append(lis[j])
if len(pair)>0:
    print(*pair)
else:
    print("No pairs found")
