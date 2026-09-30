class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array of unique integers.

        Approach:
        1. Find the pivot index (index of the minimum element / Point of Rotation)
           using binary search in O(log n) time.
        2. Once the pivot is identified, the array is effectively split into two sorted halves:
           - nums[0 ... por-1]
           - nums[por ... n-1]
        3. Determine which sorted half the target belongs to and perform standard
           binary search on that segment.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        n = len(nums)
        start = 0
        end = n - 1

        # Step 1: Find the pivot index (index of minimum element / point of rotation)
        while start < end:
            mid = (start + end) // 2
            # If mid element is greater than end element, the pivot lies in the right half
            if nums[mid] > nums[end]:
                start = mid + 1
            # Otherwise, the minimum is at mid or in the left half
            else:
                end = mid

        # 'por' (point of rotation) is the index of the smallest element
        por = start

        # Step 2: Helper function for standard binary search on subarray [left, right]
        def bs(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Step 3: Determine which sorted segment contains the target and search it

        # If array is not rotated (smallest element is at index 0), search the whole array
        if por == 0:
            return bs(0, n - 1)

        # If target lies in the right sorted portion [por, n - 1]
        if nums[por] <= target <= nums[n - 1]:
            return bs(por, n - 1)
        # Otherwise, target must be in the left sorted portion [0, por - 1]
        else:
            return bs(0, por - 1)
