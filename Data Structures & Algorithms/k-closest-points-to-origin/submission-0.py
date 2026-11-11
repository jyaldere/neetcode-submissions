import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for point in points:
            distances.append((math.sqrt(point[0]**2 + point[1]**2), point))
        heapq.heapify(distances)
        
        pts = []
        for _ in range(k):
            pts.append(heapq.heappop(distances)[1])
        return pts

