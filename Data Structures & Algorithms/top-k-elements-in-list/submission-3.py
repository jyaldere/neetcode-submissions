class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # use python Counter which translates list -> dict {count : val}

        numsDict = Counter(nums)
        topK = []
        while len(topK) < k:
            # remove max val (which is the key of the dict = count)
            # find max count, use key=numsDict.get to get the actual value of that count
            mostFrequent = max(numsDict, key=numsDict.get)
            topK.append(mostFrequent)
            # remove that max
            del numsDict[mostFrequent]

        return topK