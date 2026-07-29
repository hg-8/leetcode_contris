class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash table to store key-value pair of (number -> its index in nums) for O(1) lookup
        ht = {}
        
        # Get total count of elements to iterate over the array indices
        n = len(nums)
        
        # Initialize an empty list to hold the pair of indices that sum up to target
        ans = []
        
        # Loop through every element index in the array
        for i in range(n):
            # Calculate the required complementary value needed to reach target (key + nums[i] = target)
            key = target - nums[i]
            
            # Check if the complement has already been encountered and stored in hash table
            if key in ht:
                # If found, store the index of the complement and the current index as the result
                ans = [ht[key], i]
                # Break early since a unique solution is guaranteed
                break
            
            # Otherwise, store the current number and its index in the hash table for future element lookups
            ht[nums[i]] = i
            
        # Return the final pair of indices
        return ans