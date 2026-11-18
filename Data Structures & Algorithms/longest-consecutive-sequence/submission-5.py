class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        THIS WAS MY OG SOLUTION. O(n) memory, but O(nlogn) time because of sorted. Works, but not optimal. 
        # use hash table (dict); visited / unvisited? keep track of longest ???? this would require checking against all of those already in visited though .
        # we should take max/min from nums each time, this will ensure we dont accidentally skip a number 
        # take max, see if num+1 is in prevSeen???
        # {  }
        if nums==[]:
            return 0

        prevSeen = {} # num : num + consecutives'
        for num in sorted(nums, reverse=True):
            if num+1 in prevSeen:
                prevSeen[num] = 1 + prevSeen[num+1]
            else:
                prevSeen[num] = 1 
        return max(prevSeen.values())
    
        '''
        nums = set(nums) # remove duplicates, gives us ability to use in / not in (no need to iterate like a list)
        longest = 0

        for num in nums:
            if num-1 not in nums:  # most important. checking that the current num is not apart of chain
                length = 1
                while num+length in nums:
                    length += 1
                longest = max(longest, length)
        return longest

