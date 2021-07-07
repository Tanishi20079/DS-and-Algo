# count no. of set bits
x=int(input())
count=0
while x>0:
    count+=1
    x=x&(x-1)
print(count)
