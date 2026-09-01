class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        prev = None
        maxCount = 0
        for num in nums:
            if maxCount == 0:
                prev = num
            if num == prev:
                maxCount += 1
            else:
                maxCount -= 1
        return prev
                 