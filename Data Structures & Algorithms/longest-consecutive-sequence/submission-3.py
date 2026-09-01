class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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
