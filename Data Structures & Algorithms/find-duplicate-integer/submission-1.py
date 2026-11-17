class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # simple hash set solution O(n) memory
        '''
        seen = {}
        for num in nums:
            if num in seen:
                return num
            else:
                seen[num] = True
        '''
        # meant to use Floyds algorithm (find cycle in linked list)
        # slow pointer moves by 1
        # fast pointer moves by 2
        # once slow == fast, introduce slow 2
        # keep going until slow == slow 2
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
                     