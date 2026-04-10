import sys
from collections import deque

input = sys.stdin.readline

# Problem
# 16234 인구 이동
# https://www.acmicpc.net/problem/16234
#
# Approach
# - 각 날짜마다 BFS로 연합을 찾고, 연합 평균 인구를 temp 배열에 기록한 뒤 한 번에 반영한다.
# - 더 이상 인구 이동이 없을 때까지 날짜 수를 센다.
#
# Review
# - 동시 갱신 문제라서 board를 바로 바꾸지 않고 temp에 모아 반영하는 구조가 중요하다.

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]


def find_move():
    visited = set()
    move = False

    for r in range(N):
        for c in range(N):
            if (r, c) in visited:
                continue

            q = deque([(r, c)])
            visited.add((r, c))
            union = [(r, c)]
            union_sum = board[r][c]

            while q:
                cr, cc = q.popleft()
                cur = board[cr][cc]

                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]

                    if not (0 <= nr < N and 0 <= nc < N):
                        continue
                    if (nr, nc) in visited:
                        continue
                    if L <= abs(board[nr][nc] - cur) <= R:
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        union.append((nr, nc))
                        union_sum += board[nr][nc]

            if len(union) > 1:
                move = True
            avg = union_sum // len(union)
            for ur, uc in union:
                temp[ur][uc] = avg

    return move


answer = 0

while True:
    temp = [[0] * N for _ in range(N)]
    if not find_move():
        break
    answer += 1
    board = temp

print(answer)
