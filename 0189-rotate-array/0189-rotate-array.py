class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Normalize k using modulo in case k is greater than the size of the array
        k = k % len(nums)
        
        # Step 1: Reverse the entire array in-place
        nums.reverse()
        
        # Step 2: Reverse the first k elements to restore their original relative order
        nums[:k] = nums[:k][::-1]
        
        # Step 3: Reverse the remaining (n - k) elements to restore their original relative order
        nums[k:] = nums[k:][::-1]
        
        # Return updated array
        return nums