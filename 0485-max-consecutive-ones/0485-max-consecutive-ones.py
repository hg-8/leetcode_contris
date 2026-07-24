class Solution:
    def findMaxConsecutiveOnes(self, num: List[int]) -> int:
     ans=0
     count=0
     for i in num:   
        if i == 0:
            count = 0
        else:
            count+=1
        if(count>ans):
            ans=count
     return ans