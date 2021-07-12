# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n=int(input())
    for i in range(2,n):
        if i>(n/i):
            break
        if n%i==0:
            n=1
    if n==1:print("Not prime")
    else: print("Prime")
            
    

