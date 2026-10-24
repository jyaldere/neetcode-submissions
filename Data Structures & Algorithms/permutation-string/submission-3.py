class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = len(s1)
        i = 0
        while(i+window <= len(s2)):
            sub = s2[i:i+window]
            if sorted(s1) == sorted(sub):
                return True
            i += 1
        return False
        