import random
a=sorted(random.sample(range(1, 1001), 50))
print(a)
key=int(input("type key="))
def binary_search(a,key):
    n=len(a)
    left=0
    right=n-1
    while left<=right:
        mid=(left+right)//2
        if a[mid] < key:
            left = mid + 1
        elif a[mid] > key:
            right = mid - 1
        else:
            return mid
    return -1
print(binary_search(a,key))
