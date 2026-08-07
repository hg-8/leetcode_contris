class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater={}
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                prev=stack.pop()
                next_greater[prev]=num
            stack.append(num)
        return [next_greater.get(x,-1) for x in nums1]