class Solution:
    def sortColors(self, arr: List[int]) -> None:
        left=0
        right=len(arr)-1
        i=0
        while i<=right:
            if arr[i]==0:
                arr[left],arr[i]=arr[i],arr[left]
                left+=1
                i+=1
            elif arr[i]==2:
                arr[right],arr[i]=arr[i],arr[right]
                right-=1
            else:
                i+=1
        print(arr)
        