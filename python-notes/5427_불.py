import sys
from collections import deque

input = sys.stdin.readline

# Problem
# 5427 불
# https://www.acmicpc.net/problem/5427
#
# Approach
# - 불의 도착 시간을 멀티소스 BFS로 먼저 구한다.
# - 그다음 사람 BFS를 돌면서 불보다 먼저 도착할 수 있는 칸만 이동한다.
#
# Review
# - 기존 가지치기로도 통과는 가능했지만, 멀티소스 BFS가 문제 모델과 더 잘 맞고 구조도 깔끔하다.

drs, dcs = [-1, 0, 0, 1], [0, -1, 1, 0]


def find_fire_path():
    q = deque()

    for r in range(N):
        for c in range(M):
            if board[r][c] == "*":
                q.append((r, c))
                fire_path[r][c] = 1

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if board[nr][nc] == "#":
                continue
            if fire_path[nr][nc] > 0:
                continue

            fire_path[nr][nc] = fire_path[r][c] + 1
            q.append((nr, nc))


def survive(start):
    sr, sc = start
    q = deque([(sr, sc)])
    dist = [[0] * M for _ in range(N)]
    dist[sr][sc] = 1

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                return dist[r][c]
            if dist[nr][nc] > 0:
                continue
            if board[nr][nc] == "#":
                continue
            if 0 < fire_path[nr][nc] <= dist[r][c] + 1:
                continue

            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    return -1


T = int(input())

for _ in range(T):
    M, N = map(int, input().split())
    board = [input().strip() for _ in range(N)]
    fire_path = [[0] * M for _ in range(N)]
    start = None

    for r in range(N):
        for c in range(M):
            if board[r][c] == "@":
                start = (r, c)

    find_fire_path()
    answer = survive(start)
    print(answer if answer != -1 else "IMPOSSIBLE")
