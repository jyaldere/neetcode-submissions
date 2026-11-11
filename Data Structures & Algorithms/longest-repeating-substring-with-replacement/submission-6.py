class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0 
        longest = 0
        seen = {} # frequency map

        for i in range(len(s)):
            char = s[i]
            if char in seen:
                seen[char] += 1
            else: 
                seen[char] = 1
            while (end - start + 1) - max(seen.values()) > k:
                seen[s[start]] -= 1
                start += 1
            longest = max(longest, end - start + 1)
            end += 1
        return longest

