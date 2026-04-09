import sys

input = sys.stdin.readline

# Problem
# 17144 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144
#
# Approach
# - 한 턴을 확산, 반영, 공기청정기 작동의 세 단계로 나눈다.
# - 확산은 diff 배열에 누적한 뒤 한 번에 보드에 반영한다.
#
# Review
# - 동시 확산 문제는 보드를 직접 갱신하지 않고 변화량을 따로 모으는 편이 안전하다.

N, M, T = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dr, dc = [0, 0, -1, 1], [-1, 1, 0, 0]

cleaner = []

for r in range(N):
    for c in range(M):
        if board[r][c] == -1:
            cleaner.append((r, c))


def spread(r, c):
    remain = board[r][c]
    amount = remain // 5
    to = []

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if board[nr][nc] == -1:
            continue
        to.append((nr, nc))

    diff[r][c] -= amount * len(to)
    for nr, nc in to:
        diff[nr][nc] += amount


def cleanup():
    up_r, up_c = cleaner[0]
    down_r, down_c = cleaner[1]

    for r in range(up_r - 1, 0, -1):
        board[r][0] = board[r - 1][0]
    board[0][0] = board[0][1]

    for r in range(down_r + 1, N - 1):
        board[r][0] = board[r + 1][0]
    board[-1][0] = board[-1][1]

    for c in range(M - 1):
        board[0][c] = board[0][c + 1]
        board[-1][c] = board[-1][c + 1]
    board[0][-1] = board[1][-1]
    board[-1][-1] = board[-2][-1]

    for r in range(0, up_r):
        board[r][-1] = board[r + 1][-1]
    board[up_r][-1] = board[up_r][-2]

    for r in range(N - 1, down_r, -1):
        board[r][-1] = board[r - 1][-1]
    board[down_r][-1] = board[down_r][-2]

    for c in range(M - 1, 0, -1):
        board[up_r][c] = board[up_r][c - 1]
        board[down_r][c] = board[down_r][c - 1]
    board[up_r][1] = 0
    board[down_r][1] = 0


for _ in range(T):
    diff = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                spread(r, c)

    for r in range(N):
        for c in range(M):
            board[r][c] += diff[r][c]

    cleanup()

answer = sum(sum(row) for row in board) + 2
print(answer)
