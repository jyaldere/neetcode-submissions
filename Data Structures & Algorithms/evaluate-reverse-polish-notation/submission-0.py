class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # need 2 stacks (one for nums and one for symbol)
        # iterate through the tokens list
        # if its num, add to nums stack
        # if its a symbol pop 2 nums from num stack, append result

        nums = []
        symbols = []

        eqns = ['+', '-', '*', '/']

        for token in tokens:
            if token in eqns:
                num2 = int(nums.pop())
                num1 = int(nums.pop())
                if token == '+':
                    nums.append(num1+num2)
                elif token == '-':
                    nums.append(num1-num2)
                elif token == "*":
                    nums.append(num1*num2)
                else:
                    nums.append(num1/num2)
            else:
                nums.append(token)
                continue

        return int(nums[0])

                