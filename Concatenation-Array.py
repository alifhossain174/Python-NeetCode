class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        inputArraylegth = len(nums)
        NewArrayLength = inputArraylegth * 2

        myNewArray = []
        checkIndex = 0
        for i in range(NewArrayLength) :
            if checkIndex+1 > inputArraylegth :
                checkIndex = 0
            myNewArray.append(nums[checkIndex])
            checkIndex = checkIndex + 1
        
        return myNewArray
        