class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix product: store the product of all nums leading up to num[i]
        prefix = []
        suffix = [] 
        result = []
        currProd = 1
        for num in nums:
            currProd *= num
            prefix.append(currProd)
        currProd = 1
        for num in reversed(nums):
            currProd *= num
            suffix.append(currProd)
        suffix = list(reversed(suffix))
        result.append(suffix[1])
        for i in range(1, len(nums)-1):
            result.append(prefix[i-1]*suffix[i+1])
        result.append(prefix[len(nums)-2])
        return result




