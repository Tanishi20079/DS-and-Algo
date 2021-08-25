# Question   https://www.interviewbit.com/old/problems/spiral-order-matrix-i/

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        top,bottom,l,r=0,len(A),0,len(A[0])
        dir=0
        a=[]
        while l<=r-1 and top<=bottom-1:
            if dir==0:
                for i in range(l,r):
                    a.append(A[top][i])
                top+=1
            elif dir==1:
                for i in range(top, bottom):
                    a.append(A[i][r-1])
                r-=1
            elif dir==2:
                for i in reversed(range(l,r)):
                    a.append(A[bottom-1][i])
                bottom-=1
            elif dir==3:
                for i in reversed(range(top,bottom)):
                    a.append(A[i][l])
                l+=1
            dir=(dir+1)%4
        return a
