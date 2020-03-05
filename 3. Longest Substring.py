class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myStr = s
        myDict = {}
        
        if len(myStr) > 0:
            for i in range(0,len(myStr)):
                mySub = myStr[i]
                for j in range(i+1,len(myStr)):
                    if myStr[j] in mySub:
                        break
                    mySub = mySub + myStr[j]
                myDict[i] = len(mySub)
        else:
            myDict[0]=0

        return(max(myDict.values()))