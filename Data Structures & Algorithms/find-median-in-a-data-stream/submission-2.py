class MedianFinder:

    def __init__(self):
        # 2 heaps: smallers (max heap) and biggers (minheap)
        # they need to remain equal sizes OR max 1 size diff
        # if they ever differ more, pop a val from one to move to other
        # when u call find median, depending on sizes of both together, (if == mean of popping both, if one > than other, pop that value and return)
        self.smalls = []
        self.bigs = []
        heapq.heapify_max(self.smalls)
        heapq.heapify(self.bigs)


    def addNum(self, num: int) -> None:
        if len(self.smalls) == 0 and len(self.bigs) == 0:
            heapq.heappush_max(self.smalls, num)
            return
        if num > self.smalls[0]:
            heapq.heappush(self.bigs, num)
        else:
            heapq.heappush_max(self.smalls, num)
        
        while abs(len(self.smalls) - len(self.bigs)) > 1:
            if len(self.smalls) > len(self.bigs):
                heapq.heappush(self.bigs, heapq.heappop_max(self.smalls))
            else:
                heapq.heappush_max(self.smalls, heapq.heappop(self.bigs))

    def findMedian(self) -> float:
        total_size = len(self.smalls) + len(self.bigs)
        if total_size % 2 == 0:
            return (self.smalls[0] + self.bigs[0]) / 2
        else:
            if len(self.smalls) > len(self.bigs):
                return self.smalls[0]
            else:
                return self.bigs[0]
        
        