# 774. Minimize Max Distance to Gas Station
# Hard
# 24836FavoriteShare
# On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1], where N = stations.length.
# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.
# Return the smallest possible value of D.
# Example:
# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000
# Note:
# 1.  stations.length will be an integer in range [10, 2000].
# 2.  stations[i] will be an integer in range [0, 10^8].
# 3.  K will be an integer in range [1, 10^6].
# 4.  Answers within 10^-6 of the true value will be accepted as correct.
class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        '''
        distance = []
        for i in range(1,len(stations)):
            distance.append([-(stations[i]-stations[i-1]),1])
        heap = distance.copy()
        heapq.heapify(heap)
        for i in range(K):
            head = heapq.heappop(heap)
            head[0] = head[0]*head[1]/(head[1]+1)
            head[1] += 1
            heapq.heappush(heap, head)
        head = heapq.heappop(heap)
        return -head[0]
        '''
        distance = []
        for i in range(1,len(stations)):
            distance.append(stations[i]-stations[i-1])
        l = 0.0
        r = float(max(distance))
        while (r-l) > (10**-6):
            #print(l,r)
            mid = (l+r)/2
            cnt = 0
            result = True
            for x in distance:
                if x > mid:
                    cnt += math.ceil(x/mid)-1
                    if cnt > K: 
                        result = False
                        break
            if result: r = mid
            else: l = mid
        return (l+r)/2
