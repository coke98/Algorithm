import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# Problem
# 1520 내리막 길
# https://www.acmicpc.net/problem/1520
#
# Approach
# - dp[r][c]를 현재 칸에서 도착점까지 가는 내리막 경로 수로 둔다.
# - 더 낮은 칸으로만 이동할 수 있으므로 DFS + 메모이제이션으로 경로 수를 계산한다.
#
# Review
# - 높이가 계속 감소해서 사이클이 생기지 않으므로 DAG처럼 다룰 수 있다.

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
drs, dcs = [0, 0, 1, -1], [1, -1, 0, 0]

dp = [[-1] * M for _ in range(N)]


def dfs(r, c):
    if (r, c) == (N - 1, M - 1):
        return 1
    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for dr, dc in zip(drs, dcs):
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if board[nr][nc] < board[r][c]:
            dp[r][c] += dfs(nr, nc)

    return dp[r][c]


print(dfs(0, 0))
