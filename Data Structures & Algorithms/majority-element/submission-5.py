class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       '''
       O(n) time O(n) space
        counts = Counter(nums)
        return max(counts, key=counts.get)

       '''
       # O(n) time O(1) space
       # similar to finding max, except this is finding majority. because u are either incrementing/decrementing, u are able to go through the list once. once it hits 0 that means it is not the majority of what has been through, so it will reset and choose a new candidate (prev) . just an alg being used. 
       candidate = None
       count = 0
       for num in nums:
           if count == 0:
               candidate = num
           if num == candidate:
               count += 1
           else:
               count -= 1
       return candidate  