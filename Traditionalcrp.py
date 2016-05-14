import numpy as np

n = 10000
r = 1 #空桌子假象人数

class cluster:
    count = 0
    clusters = []
    def __str__(self):
        return str(self.count)
    def add(self, i):
        self.count += 1
        self.clusters.append(i)
        return self
    
if __name__ == "__main__":
    first = cluster().add(0) #第一位顾客选择第一个桌子
    restaurant = [first]

    for i in range(1, n):
        customerSumWithEmpty = i + r
        p = []
        for table in restaurant:
            p.append(table.count/customerSumWithEmpty)
        p.append(r/customerSumWithEmpty) #空桌子号码设为最后一个数字
        t = np.random.choice(len(p), 1, p = p)[0] #p = p
        if t == len(restaurant): #空桌子
            restaurant.append(cluster())
        restaurant[t].add(i)

    for i in restaurant:
        print(i)
