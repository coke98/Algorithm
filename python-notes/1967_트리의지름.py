import sys
from collections import defaultdict, deque

input = sys.stdin.readline

# Problem
# 1967 트리의 지름
# https://www.acmicpc.net/problem/1967
#
# Approach
# - 임의의 정점에서 가장 먼 정점을 찾고, 그 정점에서 다시 가장 먼 거리를 구한다.
# - 트리는 두 정점 사이 경로가 유일하므로, 한 번 순회하며 누적 거리만 계산하면 된다.
#
# Review
# - 가중치가 있어도 트리에서는 BFS/DFS로 누적 거리를 계산할 수 있다.

N = int(input())
adj = defaultdict(list)


def bfs(start):
    max_d = 0
    far_n = start
    q = deque([(start, 0)])
    visited = [0] * (N + 1)
    visited[start] = 1

    while q:
        n, d = q.popleft()
        for nxt, nd in adj[n]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            new_d = d + nd
            q.append((nxt, new_d))
            if new_d > max_d:
                max_d = new_d
                far_n = nxt
    return max_d, far_n


for _ in range(N - 1):
    p, c, d = map(int, input().split())
    adj[p].append((c, d))
    adj[c].append((p, d))

max_d, far_n = bfs(1)
answer, _ = bfs(far_n)
print(answer)
