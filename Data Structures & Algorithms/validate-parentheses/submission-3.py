class Solution:
    def isValid(self, s: str) -> bool:
        # stacks are lifo (pancakes)
        # push pop
        
        # read through the string s
        # append to a list each value. 
        # need to be able to peek at top of the stack
            # if peek = opening and next s = closing of same time, POP
            # else, return false
        # {[()]}([{}]){([])}
        # {[}]
        stack = []
        openings = ['(', '{', '[']
        closings = [')', '}', ']']
        if len(s) < 2:
            return False
        for char in s:
            if char in openings:
                stack.append(char)
            elif char in closings:
                if len(stack) < 1:
                    return False
                if stack[-1] == '(' and char == ')':
                    stack.pop()
                    continue
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                    continue
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                    continue
                return False
        if len(stack) != 0:
            return False
        return True
            
        