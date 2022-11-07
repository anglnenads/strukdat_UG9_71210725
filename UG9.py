class Node:
    def __init__(self,data,priority):
        self._data = data
        self._priority = priority

class PriorityQueueSortedList:

    def __init__(self):
        self._data = []
    
    def peek(self):
        print("Data prioritas tertinggi : ", self._data[0])

    def add(self, dataBaru, prioBaru):
        if len(self._data):
            baru = 0
            while self._data[baru][1] < prioBaru:
                baru += 1
            self._data.insert(baru, (dataBaru, prioBaru))
        else:
            self._data.append((dataBaru, prioBaru))

    def update(self, prioBaru, dataBaru):
        baru = 0
        while self._data[baru][1] != prioBaru:
            baru += 1
        self._data[baru] = (dataBaru, prioBaru)
    
    def remove(self):
        del self._data[0]
        

    def removePriority(self, prio):
        baru = 0
        while self._data[baru][1] != prio:
            baru += 1
        del self._data[baru]

    def printAll(self):
        print("Isi semua  : ", end="")
        for i in self._data[:-1]:
            print("{}," .format(i), end=" ")
        print("{}" .format(self._data[-1]))


sortedList = PriorityQueueSortedList()
sortedList.add("Shalom", 5)
sortedList.add("Beatrix", 1)
sortedList.add("Sindu", 3)
sortedList.add("Hanif", 2)
sortedList.add("Dedi", 4)
sortedList.update(4, "Karin")
sortedList.update(3, "Rafi")
sortedList.remove()
sortedList.removePriority(4)
sortedList.peek()
sortedList.printAll()