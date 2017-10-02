def rm_small(mylist):
    if len(mylist) <= 1:
        return []
    else:
        min_number = mylist.index(min(mylist))
        del mylist[min_number]
        return mylist

print(rm_small([1,2,3,4]))
print(rm_small([6,5,4,3,2,1]))