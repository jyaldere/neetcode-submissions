class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack is lifo
        # for each temp in temperatures, how many days need to pass until we hit a temp that is greater than current temp 
        # if none, 0
        # okay it makes sense: going from the back, we add them to a non increasing stack
        # as you are swapping the curr value in order to get it to the right place, keep a counter 
        # once it hits its proper place, results[i] = that counter 

        stack = [] # should we just go from end to start since thats the way we are iterating the temps?
        results = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[i]

            while stack and temp >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                results[i] = stack[-1] - i
            stack.append(i)
        return results
