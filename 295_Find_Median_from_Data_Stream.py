class MedianFinder:
    from heapq import heappush, heappop
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # idea is always push to small. however, when push to small, we want to check if num is larger than mininum in large.
        # instead of pop large[0] (which may not exists) to compare, use heappush pop is a very smart operation which directly return the smallest one between large[0] and num
        heappush(self.small, -heappushpop(self.large, num))
        if len(self.small) > (len(self.large) + 1):
            heappush(self.large, -heappop(self.small))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()