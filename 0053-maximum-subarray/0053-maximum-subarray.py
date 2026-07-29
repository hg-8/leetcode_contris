class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize maxsofar with the first element to track overall maximum subarray sum
        maxsofar = nums[0]
        
        # Initialize currentsum with the first element to track running sum of current contiguous subarray
        currentsum = nums[0]
        
        # Loop through array starting from second element (index 1)
        for i in range(1, len(nums)):
            # If previous running sum is negative, reset currentsum to 0 (discard negative contribution)
            if currentsum < 0:
                currentsum = 0
                
            # Add current element to running subarray sum
            currentsum += nums[i]
            
            # Update maxsofar if the current subarray sum exceeds maximum seen so far
            if currentsum > maxsofar:
                maxsofar = currentsum
                
        # Return global maximum subarray sum found
        return maxsofar