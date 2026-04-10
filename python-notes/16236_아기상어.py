import sys
from collections import deque

input = sys.stdin.readline

# Problem
# 16236 아기 상어
# https://www.acmicpc.net/problem/16236
#
# Approach
# - 매번 BFS로 먹을 수 있는 물고기 중 가장 가까운 물고기를 찾는다.
# - 같은 거리라면 가장 위쪽, 그다음 가장 왼쪽 물고기를 선택한다.
#
# Review
# - 이 문제는 BFS 자체보다 후보 우선순위와 상어의 크기/경험치 상태 관리가 핵심이다.

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
drs, dcs = [-1, 0, 0, 1], [0, -1, 1, 0]

shark = (-1, -1)
size = 2
exp = 0

for r in range(N):
    for c in range(N):
        if board[r][c] == 9:
            shark = (r, c)


def movetofish():
    global shark
    global size
    global exp

    fish = (N, N)
    min_dist = float('inf')

    sr, sc = shark
    q = deque([(sr, sc, 0)])
    visited = set()
    visited.add((sr, sc))

    while q:
        r, c, d = q.popleft()
        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if (nr, nc) in visited:
                continue
            if board[nr][nc] > size:
                continue

            nd = d + 1

            if 0 < board[nr][nc] < size:
                if nd < min_dist:
                    fish = (nr, nc)
                    min_dist = nd
                elif nd == min_dist:
                    fr, fc = fish
                    if nr < fr:
                        fish = (nr, nc)
                    elif fr == nr and nc < fc:
                        fish = (nr, nc)
                continue

            if min_dist != float("inf"):
                continue

            q.append((nr, nc, nd))
            visited.add((nr, nc))

    if fish != (N, N):
        fr, fc = fish
        shark = fish
        exp += 1
        if exp == size:
            exp = 0
            size += 1
        board[fr][fc] = 9
        board[sr][sc] = 0

    return min_dist if min_dist != float('inf') else 0


answer = 0

while True:
    sec = movetofish()
    if sec == 0:
        break
    answer += sec

print(answer)
