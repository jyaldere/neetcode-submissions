class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if sorted(set(nums)) != sorted(nums):
            return True
        else:
            return False
        