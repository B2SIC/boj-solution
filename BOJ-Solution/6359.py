count = int(input())
answer_list = []

for l in range(count):

    n = int(input())

    room_list_closed = []
    room_list_opend = []

    for i in range(1, n+1):
        room_list_opend.append(i)

    for j in range(2, n+1):
        for k in range(j, n+1, j):
            if k in room_list_opend:
                room_list_closed.append(k)
                room_list_opend.remove(k)
            else:
                room_list_opend.append(k)
                room_list_closed.remove(k)

    answer_list.append(len(room_list_opend))

for a in answer_list:
    print(a)

