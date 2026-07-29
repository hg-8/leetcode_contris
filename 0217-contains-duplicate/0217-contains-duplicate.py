class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize empty hash map (or set lookup) to track numbers seen so far
        map = {}
        
        # Iterate over each number in the array
        for num in nums:
            # If current number has not been encountered yet, add it to hash map
            if num not in map:
                map[num] = 1
            # If current number is already present in hash map, duplicate is found
            else:
                return True
                
        # If loop completes without finding any duplicates, return False
        return False