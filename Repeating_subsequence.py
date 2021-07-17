# Input 1: A = "abab"
# Output 1: True as "ab" is repeating subsequence

# Input 2:  A = "abba"
# Output 2: False


class Solution:
	# @param A : string
	# @return an integer
	def anytwo(self, A):
	    B=A
        lcs=[[-1 for i in range(len(A)+1)]for j in range(len(B)+1)]
        for i in range(len(A)):
            for j in range(len(B)):
                if i==0 or j==0:
                    lcs[i][j]=0
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                if A[i-1]==B[j-1] and i!=j:
                    lcs[i][j]=1+lcs[i-1][j-1]
                else:
                    lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
        # print(lcs[len(A)][len(B)])
                  
        if lcs[len(A)][len(B)]>1:
            return 1
        return 0
