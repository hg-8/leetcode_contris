class Solution:
        def nextGreaterElements(self, A):
            stack, res = [], [-1] * len(A)
            for i in range((len(A)) * 2):
                i=i%len(A)
                while stack and (A[stack[-1]] < A[i]):
                    temp=stack.pop()
                    res[temp] = A[i]
                    print(temp)
                stack.append(i)
            print(stack)
            return res
        