# Shallow copy and deep copy in python list

import copy

"""A shallow copy of an object is a copy whose properties share the same references point to the same underlying values) as those of the source object from which the copy was made.

A deep copy of an object is a copy whose properties do not share the same references (point to the same underlying values) as those of the source object from which the copy was made
"""

# Shallow copy
# Any change in the nested list of parent_lst will also show up in the shallow_copy list
print()
parent_lst = [1,2,[1,2,3],[6,5,2],[1,2],9,8] 
print("---------- Shallow copy ---------")
shallow_copy = copy.copy(parent_lst)
parent_lst[2][1]="A"
parent_lst[3][2]="B"        # Making changes in the parent_lst
print("Parent list -->",parent_lst)
print("Shallow copy list -->",shallow_copy)
print()
print()
# Deep copy
# Any change in the nested list of parent_lst wil not make any changes in the deep_copy list
print("---------- Deep copy -----------")
parent_lst=[1,2,[1,2,3],[6,5,2],[1,2],9,8] 
deep_copy = copy.deepcopy(parent_lst)
parent_lst[2][2]="A"
parent_lst[3][1]="B"            # Making changes in the parent_lst
print("Parent list -->",parent_lst)
print("Deep copy list -->",deep_copy)