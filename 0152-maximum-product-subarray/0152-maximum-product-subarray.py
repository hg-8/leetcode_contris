class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Track max sub-product ending at current position
        maxprod = nums[0]
        
        # Track min sub-product ending at current position (handling negative values flipping signs)
        minprod = nums[0]
        
        # Track global maximum product overall
        result = nums[0]
        
        # Loop through array starting from second element (index 1)
        for i in range(1, len(nums)):
            # Case 1: Current number is non-negative (doesn't flip min/max roles)
            if nums[i] >= 0: 
                maxprod = max(maxprod * nums[i], nums[i])
                minprod = min(minprod * nums[i], nums[i])
            # Case 2: Current number is negative (flips min product into max product and vice-versa)
            else:
                temp = maxprod  # Save previous maxprod before overwriting
                maxprod = max(minprod * nums[i], nums[i])
                minprod = min(temp * nums[i], nums[i])
                
            # Update global result with maximum product obtained so far
            result = max(result, maxprod)
            
        # Return global max product subarray result
        return result