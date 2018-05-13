class Distance:
    def __init__(self):
        self.store_list = []

    def getDistance(self, get_list):
        for i in range(len(get_list)):
            sum = 0
            for j in range(len(get_list[i])):
                sum += get_list[i][j]
            self.store_list.append(sum)
        self.getMin()

    def getMin(self):
        if self.store_list[0] < self.store_list[1]:
            if self.store_list[0] < self.store_list[2]:  # Min: A
                print("A %d" % self.store_list[0])
        elif self.store_list[1] < self.store_list[0]:
            if self.store_list[1] < self.store_list[2]:  # Min: B
                print("B %d" % self.store_list[1])
        elif self.store_list[2] < self.store_list[0]:
            if self.store_list[2] < self.store_list[1]:  # Min: C
                print("C %d" % self.store_list[2])


d1 = Distance()
d1.getDistance([[1,3], [3,5], [2,4]])

d2= Distance()
d2.getDistance([[3,7], [1,1], [2,5]])
