class Solution:
    def sortColors(self, arr: List[int]) -> None:
        # Dutch National Flag Algorithm (Three-pointer approach)
        # 'left' pointer tracks boundary for 0s (red color)
        left = 0
        
        # 'right' pointer tracks boundary for 2s (blue color)
        right = len(arr) - 1
        
        # 'i' pointer traverses array elements from left to right
        i = 0
        
        # Continue loop until scanning pointer 'i' passes the 'right' boundary pointer
        while i <= right:
            # Case 1: Element is 0 -> swap to front (left boundary)
            if arr[i] == 0:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1  # Expand 0s section to right
                i += 1     # Advance scanner as swapped element at i is known to be 1 or 0
            # Case 2: Element is 2 -> swap to back (right boundary)
            elif arr[i] == 2:
                arr[right], arr[i] = arr[i], arr[right]
                right -= 1 # Expand 2s section to left (do not advance i yet, need to inspect swapped element)
            # Case 3: Element is 1 -> already in middle section
            else:
                i += 1     # Simply advance scanner pointer
                
        # Optional print output for visual confirmation
        print(arr)