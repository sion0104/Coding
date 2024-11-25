import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    nums = map(int, input().split())

    for num in nums:
        if len(heap) >= N:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        else:
            heapq.heappush(heap, num)

print(heap[0])
