for _ in range(int(input())) :
    n=int(input())
    s=list(map(int,input().split()))
    d=(s[-1]-s[0])//n
    for i in range(n):
        if s[i]!=s[0]+i*d:
            print(s[0]+i*d);break
