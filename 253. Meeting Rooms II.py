# 253. Meeting Rooms II
# Medium
# 156426FavoriteShare
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.
# Example 1:
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:
# Input: [[7,10],[2,4]]
# Output: 1
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        max_room = 0
        for start,stop in intervals:
            if len(heap) == 0: heapq.heappush(heap, stop)
            else:
                while len(heap) != 0 and heap[0] <= start:
                    heapq.heappop(heap)
                heapq.heappush(heap, stop)
            current_room = len(heap)
            if current_room > max_room: max_room = current_room
            #print(heap)
        return max_room
        
