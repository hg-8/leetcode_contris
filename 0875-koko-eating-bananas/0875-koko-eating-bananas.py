class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        start=1
        end=max(piles)
        ans=end
        while start<=end:
           mid=(start+end)//2
           if (self.timetaken(piles,mid)>h):
                start=mid+1
           else:
                ans=mid
                end=mid-1
        return ans
    def timetaken(self,piles,speed):
        totaltime=0
        for pile in piles:
            totaltime+=math.ceil(pile/speed)
        return totaltime