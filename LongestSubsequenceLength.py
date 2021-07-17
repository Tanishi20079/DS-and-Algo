# Given an 1D integer array A of length N, find the length of longest subsequence which is first increasing then decreasing.
# Input:  A = [1, 2, 1]
# Output: 3


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestSubsequenceLength(self, A):
	    lenA = len(A)
        lA =list(A)
        if lenA ==0: return 0
        if lenA == 1: return 1
        rA= list(A)
        rA.reverse()
        B = [1] * lenA
        C = [1] * lenA
        for i in range(1,lenA):
            for j in range(0, i):
                # print(j, i)
                if lA[i] > lA[j] and B[i] < B[j] + 1:
                    B[i] = B[j] + 1
                # print(B)
                if rA[i] > rA[j] and C[i] < C[j] +1:
                    C[i] =C[j] +1
        C.reverse()
        final = [0]*lenA
        for i in range(0,lenA):
            final[i] = B[i]+ C[i] -1
        return max(final)
