def findKim(seoul):
    kim_idx = 0

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            kim_idx = i

    return "김서방은 {}에 있다".format(kim_idx)

'''
More efficient Code
def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index("Kim"))
'''

print(findKim(["Queen", "Tod", "Kim"]))
