import sys
import heapq


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        weight, now = heapq.heappop(heap)

        if dp[now] < weight:
            continue

        for w, next_node in graph[now]:
            next_weight = w + weight
            if next_weight < dp[next_node]:
                dp[next_node] = next_weight
                heapq.heappush(heap, (next_weight, next_node))


input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
dp = [INF] * (V + 1)
heap = []

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])
