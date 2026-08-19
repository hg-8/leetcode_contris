"""
Python `enumerate` Practice Problems
------------------------------------
Fill in your implementations in the functions below.
When you're ready, let me know and I will run test cases to verify your code!
"""

from typing import List, Tuple, Optional


# ==============================================================================
# Problem 1: Find All Target Indices (Warm-up)
# ==============================================================================
# Task: Given a list of integers `nums` and an integer `target`,
#       return a list of all 0-based indices where `target` appears.
#
# Example:
#   nums = [10, 20, 30, 20, 40, 20], target = 20
#   Output: [1, 3, 5]
# ==============================================================================
def find_all_indices(nums: List[int], target: int) -> List[int]:
    # TODO: Use enumerate(nums)
    output=[]
    for index,num in enumerate(nums):
        if num==target:
            output.append(index)
    return output
    pass


# ==============================================================================
# Problem 2: Leaderboard Formatter (Custom Start Index)
# ==============================================================================
# Task: Given a list of player names and a starting rank `start_rank` (default 1),
#       return a list of formatted strings in the format: "<rank>. <name>"
#       Hint: Remember `enumerate(iterable, start=...)`.
#
# Example:
#   names = ["Alice", "Bob", "Charlie"], start_rank = 1
#   Output: ["1. Alice", "2. Bob", "3. Charlie"]
#
#   names = ["David", "Eve"], start_rank = 10
#   Output: ["10. David", "11. Eve"]
# ==============================================================================
def format_leaderboard(names: List[str], start_rank: int = 1) -> List[str]:
    # TODO: Use enumerate(names, start=...)
    output=[]
    for index,name in enumerate(names):
        output.append(f"{index+start_rank}. {name}")
    return output
    pass


# ==============================================================================
# Problem 3: Elements Greater Than Index
# ==============================================================================
# Task: Given a list of numbers, return a list of tuples `(index, value)` for
#       all elements where the element's value is strictly greater than its index.
#
# Example:
#   nums = [-1, 0, 5, 2, 8, 4]
#   Indices: 0   1  2  3  4  5
#   - index 2: value 5 > 2  -> (2, 5)
#   - index 4: value 8 > 4  -> (4, 8)
#   Output: [(2, 5), (4, 8)]
# ==============================================================================
def elements_greater_than_index(nums: List[int]) -> List[Tuple[int, int]]:
    # TODO: Use enumerate(nums)
    output=[]
    for index,num in enumerate(nums):
        if num>index:
            output.append((index,num))
    return output
    pass


# ==============================================================================
# Problem 4: Two Sum (Hash Map + Enumerate)
# ==============================================================================
# Task: Given an array of integers `nums` and an integer `target`,
#       return the indices [i, j] of the two numbers such that they add up to target.
#       Each input has exactly one solution, and you may not use the same element twice.
#
# Example:
#   nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1] (or [1, 0])
#
#   nums = [3, 2, 4], target = 6
#   Output: [1, 2]
# ==============================================================================
def two_sum(nums: List[int], target: int) -> Optional[List[int]]:
    # TODO: Use enumerate(nums) with a dictionary
    lt=list(enumerate(nums))
    ht={}
    for index,num in lt:
        key=target-num
        if key in ht:
            return [ht[key],index]
        ht[num]=index
    pass


# ==============================================================================
# Problem 5: Find Character Coordinates in a 2D Grid
# ==============================================================================
# Task: Given a 2D grid of characters (list of strings or list of lists) and a target
#       character `char`, return a list of (row_index, col_index) coordinates
#       where `char` is found.
#
# Example:
#   grid = [
#       ["A", "B", "A"],
#       ["C", "A", "D"],
#       ["E", "F", "G"]
#   ]
#   char = "A"
#   Output: [(0, 0), (0, 2), (1, 1)]
# ==============================================================================
def find_char_coordinates(grid: List[List[str]], char: str) -> List[Tuple[int, int]]:
    # TODO: Use nested enumerate()
    output=[]
    for i,row in enumerate(grid):
        for j,col in enumerate(row):
            if col == char:
                output.append((i,j))
    return output
    pass
