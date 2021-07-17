class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        B=''.join(reversed(A))
        lcs=[[-1 for i in range(len(A)+1)]for j in range(len(B)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if i==0 or j==0:
                    lcs[i][j]=0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1]:
                    lcs[i][j]=1+lcs[i-1][j-1]
                else:
                    lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
                    
        return lcs[len(A)][len(B)]
