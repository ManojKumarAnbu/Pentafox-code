alp=list(map(int,input("Enter the numbers 1-26").split(",")))
for i in range(len(alp)):
    print(chr(64+alp[i]))
