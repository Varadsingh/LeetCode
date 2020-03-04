class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}
        comp = 0
        for i in range(0,len(nums)):
            comp = target - nums[i]
            if comp in myDict.values():
                j = list(myDict.values()).index(comp)
                return([i,j])
            myDict[i] = nums[i]