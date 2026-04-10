import sys
from collections import deque

input = sys.stdin.readline

# Problem
# 2638 치즈
# https://www.acmicpc.net/problem/2638
#
# Approach
# - 매 시간마다 외부 공기를 BFS로 찾고, 그 공기와 두 면 이상 맞닿은 치즈를 녹인다.
# - 더 이상 녹을 치즈가 없을 때까지 반복한다.
#
# Review
# - 종료 조건은 전체 칸 수를 세는 방식보다 `이번 턴에 녹을 치즈가 있는가`로 잡는 편이 안전하다.

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
drs, dcs = [0, 0, -1, 1], [-1, 1, 0, 0]


def find_air():
    air = set([(0, 0)])
    q = deque([(0, 0)])

    while q:
        r, c = q.popleft()

        for dr, dc in zip(drs, dcs):
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if (nr, nc) in air:
                continue
            if board[nr][nc] == 0:
                q.append((nr, nc))
                air.add((nr, nc))

    return air


def find_remove(air):
    res = []

    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:
                cnt = 0
                for dr, dc in zip(drs, dcs):
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in air:
                        cnt += 1
                        if cnt > 1:
                            res.append((r, c))
                            break
    return res


answer = 0

while True:
    air = find_air()
    remove = find_remove(air)

    if not remove:
        break

    for rr, rc in remove:
        board[rr][rc] = 0

    answer += 1

print(answer)
