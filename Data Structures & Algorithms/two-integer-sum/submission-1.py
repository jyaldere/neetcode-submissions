class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # u have a dict of { val: index}
        prevMap = {}
        for i, val in enumerate(nums):
            # u take the diff of target and current number which = number u need for it to be 2 sum
            diff = target-val

            #check if you've seen this already instantly with dict, no need to compare every num to every other num 
            if diff in prevMap:
                return [prevMap[diff], i]
            
            # if u havent seen its complement yet, add it for future consideration 
            prevMap[val] = i
        return