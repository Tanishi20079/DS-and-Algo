# count no. of set bits or count no. of 1s
x=int(input())
count=0
while x>0:
    count+=1
    x=x&(x-1)
print(count)
