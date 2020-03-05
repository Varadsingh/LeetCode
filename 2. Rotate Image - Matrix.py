class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        myArr = matrix
        maxR = len(myArr)
        maxC = len(myArr[0])


        for i in range(maxR):
            myArr.append([0]*maxC)

        for i in range(maxR):
            for j in range(maxC):
                myArr[j+maxR][maxC-i-1] = myArr[i][j]

        for i in range(maxR):
            myArr.pop(0)