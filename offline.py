# #stacks
# # lifo -last in first out
# # adt - abstract data type
# from time import time
# three method will always be there:
# i) push(x) - insert element x into the stack, o(1) time 
# ii)pop(x) - remove the last inserted element,o(1) time
# iii)top(x)- access last inserted element,o(1) time
# push(10)
# implementing ways of stacks:
# 1.linked list 
# 2.arrays
#stack when using list
# st=[]
# st.append(10)
# st.append(15)
# st.append(20)
# st.append(2)
# print(st[len(st)-1])
#deque - double ended que
# it supports push and pop from both sides(we can do push and pop from start and also end of the stack) 
from collections import deque
st=deque()
st.append(10)
st.append(15)
st.append(20)
st.append(2)
print(st[-1])
#good for large dataset


