import sys

input = sys.stdin.readline

# Problem
# 2579 계단 오르기
# https://www.acmicpc.net/problem/2579
#
# Approach
# - dp[i]를 i번째 계단에 도달했을 때 얻을 수 있는 최대 점수로 둔다.
# - 마지막 계단은 반드시 밟아야 하므로, 현재 계단에 도달하는 두 경우만 비교한다.
#
# Review
# - `3연속 금지`와 `마지막 계단 필수`를 함께 반영하면 점화식이 2개 케이스로 정리된다.

N = int(input())

floor = [int(input()) for _ in range(N)]
dp = [0] * N

for i in range(N):
    if i == 0:
        dp[0] = floor[0]
    elif i == 1:
        dp[1] = dp[0] + floor[1]
    elif i == 2:
        dp[2] = max(floor[2] + floor[1], dp[0] + floor[2])
    else:
        case1 = dp[i - 3] + floor[i - 1] + floor[i]
        case2 = dp[i - 2] + floor[i]

        dp[i] = max(case1, case2)

print(dp[N - 1])
