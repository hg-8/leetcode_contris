class Solution:
    def addtodict(self,ht,ch):
        if ch not in ht:
            ht[ch]=1
        else:
            ht[ch]+=1
    def remove(self,ht,ch):
        ht[ch]-=1
    def valid(self,ht):
        for ch in ht:
            if ht[ch] >1:
                return False    
        return True
    def lengthOfLongestSubstring(self, s: str) -> int:
        fp=0
        sp=0
        ht={}
        ans=0
        n=len(s)
        while sp<n:
            self.addtodict(ht,s[sp])
            while(fp<sp and not self.valid(ht)):
                self.remove(ht,s[fp])
                fp+=1
            length = sp-fp+1
            ans=max(ans,length)
            sp+=1
        return ans
