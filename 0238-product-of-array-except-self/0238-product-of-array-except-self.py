class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[List[int]]:
        # Get total length of input array
        n = len(nums)
        
        # Initialize left prefix product array with default 1s
        left = [1] * n
        
        # Initialize right suffix product array with default 1s
        right = [1] * n
        
        # Build prefix products (left to right) and suffix products (right to left) simultaneously
        for i in range(1, n):
            # left[i] contains product of all elements to the left of index i
            left[i] = left[i - 1] * nums[i - 1]
            
            # right[-(i+1)] contains product of all elements to the right of index (n - 1 - i)
            right[-(i + 1)] = right[-i] * nums[-i]
            
        # Initialize output array
        output = []
        
        # Combine prefix and suffix products for each index to get total product except self
        for i in range(0, n):
            output.append(left[i] * right[i])
            
        # Return final product array
        return output