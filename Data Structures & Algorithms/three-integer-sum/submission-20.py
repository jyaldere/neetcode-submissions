class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) time O(1) space
        # -4 -1 -1 0 1 2
        # 2 pointers start vs end
        # pointer than will move through the array + 2 others that will be its complements
        # repeat
        # inefficient

        nums.sort()
        result = []

        for i in range(len(nums)):

            main = nums[i]
            # main is the smallest of the nums we are tracking. once its positive, another threeSum DNE, break
            if main > 0:
                break

            # skip duplicate i's
            if i > 0 and main == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            while l < r:
                left = nums[l]
                right = nums[r]
                total = main+left+right
                if total < 0:
                    l += 1
                elif total > 0: 
                    r -= 1
                else:
                    result.append([main, left, right])
                    l += 1
                    r -= 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result



                

