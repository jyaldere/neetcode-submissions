class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # seenSubstrings are going to track substrings
        # need 2 pointers; start/end of the substring 
            # if u encounter a char in the substring, shift the start ptr to after its first occurence 
            # still keep track of longest
        start = 0
        seenSubstring = {}
        longest = 0
        for i in range(len(s)):
            if s[i] in seenSubstring:
                start = max(start, seenSubstring[s[i]] + 1)
            seenSubstring[s[i]] = i
            longest = max(longest, i - start + 1)
        return longest