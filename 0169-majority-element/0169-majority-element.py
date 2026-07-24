class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        mc=arr[0]
        c=1
        for i in range(1,len(arr)):
            if (arr[i]==mc):
                c+=1
            else:
                c-=1
                if (c==0):
                    mc=arr[i]
                    c=1            
        print(mc)
        return mc