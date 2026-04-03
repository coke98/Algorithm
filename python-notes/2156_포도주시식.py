import sys

input = sys.stdin.readline

# Problem
# 2156 포도주 시식
# https://www.acmicpc.net/problem/2156
#
# Approach
# - dp[i]를 i번째 잔까지 봤을 때 마실 수 있는 최대 양으로 둔다.
# - 현재 잔을 마시는 경우 2개와 마시지 않는 경우 1개로 나눠 점화식을 세운다.
#
# Review
# - `3잔 연속 금지`는 현재 잔 기준으로 경우를 나누면 점화식이 선명해진다.

N = int(input())

wines = [int(input()) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[0] = wines[0]
    elif i == 1:
        dp[1] = dp[0] + wines[1]
    elif i == 2:
        dp[2] = max(wines[2] + wines[1], dp[0] + wines[2], dp[1])
    else:
        case1 = dp[i - 3] + wines[i - 1] + wines[i]
        case2 = dp[i - 2] + wines[i]
        case3 = dp[i - 1]

        dp[i] = max(case1, case2, case3)

print(dp[N - 1])
