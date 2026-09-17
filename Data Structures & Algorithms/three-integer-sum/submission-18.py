class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(n^2) time O(1) space
        # -4 -1 -1 0 1 2
        # 2 pointers start vs end
        # pointer than will move through the array + 2 others that will be its complements
        # repeat
        # inefficient

        nums.sort()
        i = 0
        l = 1
        r = len(nums) - 1
        result = []

        while i <= len(nums) - 3:

            if l >= r:
                i += 1
                while i <= len(nums) - 3 and nums[i] == nums[i - 1]:
                    i += 1
                l = i + 1
                r = len(nums) - 1
                continue

            main = nums[i]
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



                

