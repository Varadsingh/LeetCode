# 996. Number of Squareful Arrays
# Given an array A of non-negative integers, the array is squareful if for every pair of adjacent elements, their sum is a perfect square.

# Return the number of permutations of A that are squareful.  Two permutations A1 and A2 differ if and only if there is some index i such that A1[i] != A2[i].

 

# Example 1:

# Input: [1,17,8]
# Output: 2
# Explanation: 
# [1,8,17] and [17,8,1] are the valid permutations.
# Example 2:

# Input: [2,2,2]
# Output: 1
 

# Note:

# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9

class Solution:
    # @param A : list of integers
    # @return an integer      
    def numSquarefulPerms(self, A: List[int]) -> int:
        myCount = {}
        mySqrs = {}
        for i in A:
            myCount[i] = A.count(i)
            mySqrs[i] = []
        for i in myCount.keys():
            for j in myCount.keys():
                tmpSum = i + j
                tmpSqrt = int(tmpSum ** 0.5)
                if tmpSqrt**2 == tmpSum:
                    mySqrs[i].append(j)
        mySum = 0
        def myDef(i,r):
            myCount[i] = myCount[i] - 1
            if r == 0:
                myAns = 1
            else:
                myAns = 0
                for x in mySqrs[i]:
                    if myCount[x]:
                        myAns = myAns + myDef(x,r-1)
            myCount[i] = myCount[i] + 1
            return(myAns)
        for i in myCount.keys():
            mySum = mySum + myDef(i,len(A)-1)
        del tmpSqrt,tmpSum
        return(mySum)