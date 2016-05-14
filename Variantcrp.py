n = 10000

class cluster:
    count = 0
    clusters = []
    def __str__(self):
        return str(self.count)
    def add(self, i):
        self.count += 1
        self.clusters.append(i)
        return self

def getSim(v, table):
    #相似性函数，返回概率值
    pass

def getVec():
    #载入向量
    pass

if __name__ == "__main__":
    V = getVec() #向量集合
    first = cluster().add(0) #第一位顾客选择第一个桌子
    restaurant = [first]

    for i in range(1, n):
        p = []
        pn = 1.0/(1 + len(restaurant))
        for table in restaurant:
            p.append(getSim(V[i], table))
        maxVal = max(p)
        maxIdx = p.index(maxVal)
        if maxVal < pn:
            if random.uniform(0,1) < pn:#创造桌子
                new = cluster().add(i)
                restaurant.append(new)
        restaurant[maxIdx].add(i)

    for i in restaurant:
        print(i)
