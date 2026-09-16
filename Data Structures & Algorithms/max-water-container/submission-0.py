class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # off the bat, 2 pointers starting from start/end of list
        # you would have maxleft and maxright to compute max are
        # its |i-j| * min(height1, height2) 
        # i would then move both in (i+1, j-1) and recompute, if 
        # changing one or the other computes a greater area then
        # update maxleft or maxright
        # compute white i < j

        # pointers (storing optimal heights (index))
        maxLeft, maxRight, maxArea = 0, 0, 0

        i = 0
        j = len(heights) - 1

        while (i < j):
            minHeight = min(heights[i], heights[j])
            area = abs(i-j) * minHeight

            if (area > maxArea):
                maxArea = area
                maxLeft = i
                maxRight = j
            if minHeight == heights[i]:
                i += 1
            elif minHeight == heights[j]:
                j -= 1
            
        
        return maxArea