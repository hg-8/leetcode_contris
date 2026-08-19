class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ht={}
        for index,number in enumerate(numbers):
            key=target-number
            if key in ht:
                return [ht[key]+1,index+1]
            ht[number]=index