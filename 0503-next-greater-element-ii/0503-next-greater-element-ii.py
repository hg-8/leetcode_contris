class Solution:
        def nextGreaterElements(self, A):
            stack, res = [], [-1] * len(A)
            for i in range((len(A)) * 2):
                curr_index=i%len(A)
                while stack and (A[stack[-1]] < A[curr_index]):
                    temp=stack.pop()
                    res[temp] = A[curr_index]
                    print(temp)
                if i<len(A):
                    stack.append(curr_index)
            print(stack)
            return res
        