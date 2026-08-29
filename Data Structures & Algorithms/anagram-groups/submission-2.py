class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {} # sortedWord : [ list of anagrams ]

        for word in strs:
            # for every word take it and sort the letters in the word. cat -> act
            sortedWord = ''.join(sorted(word))
            
            # add it to the dict. dict is a way to keep track of the words that are anagrams of each other
            if sortedWord in words:
                words[sortedWord].append(word)
            else:
                words[sortedWord] = [word]
        # convert just the values (not keys) of dict to nested list
        return list(words.values())
