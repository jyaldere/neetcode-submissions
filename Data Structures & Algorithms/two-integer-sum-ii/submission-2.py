class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # this is a 2 pointer problem, meaning the 2 pointers are likely the 
        # greater index and smaller index. 
        # since the list is sorted, we can cut off the list where list[i] > target (binary search)

        # starting at smallest number and largest number (w pointers) we will move the smaller idx up if the sum between list[smaller] + list[larger] < target
        # and vice versa 

        smaller = 0
        #i = len(numbers) - 1
        #while numbers[i] > target and i >= 0:
        #    i -= 1
        #larger = i
        larger = len(numbers) - 1

        while smaller < larger:
            candidate = numbers[smaller] + numbers[larger]
            if candidate > target:
                larger -= 1
            elif candidate < target:
                smaller += 1
            else:
                return [smaller+1, larger+1]
        return [smaller+1, larger+1]

