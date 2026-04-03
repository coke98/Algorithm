import sys

input = sys.stdin.readline

# Problem
# 9465 스티커
# https://www.acmicpc.net/problem/9465
#
# Approach
# - dp[0][i], dp[1][i]를 각각 i번째 열까지 봤을 때 마지막에 위/아래 스티커를 고른 최대 점수로 둔다.
# - 현재 열에서 위나 아래를 고를 때 올 수 있는 이전 상태를 비교해 점화식을 세운다.
#
# Review
# - 현재 열에서 위를 고를지 아래를 고를지로 상태를 나누면 인접 금지 조건을 다루기 편하다.


def solve():
    N = int(input())
    st = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * N for _ in range(2)]

    for i in range(N):
        if i == 0:
            dp[0][0] = st[0][0]
            dp[1][0] = st[1][0]
        elif i == 1:
            dp[0][1] = st[0][1] + dp[1][0]
            dp[1][1] = st[1][1] + dp[0][0]
        else:
            case1 = st[0][i] + dp[1][i - 1]
            case2 = st[0][i] + max(dp[0][i - 2], dp[1][i - 2])
            case3 = st[1][i] + dp[0][i - 1]
            case4 = st[1][i] + max(dp[0][i - 2], dp[1][i - 2])
            dp[0][i] = max(case1, case2)
            dp[1][i] = max(case3, case4)

    print(max(dp[0][N - 1], dp[1][N - 1]))


T = int(input())
for _ in range(T):
    solve()
