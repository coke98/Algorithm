import sys
import heapq

input = sys.stdin.readline

# Problem
# 13904 과제
# https://www.acmicpc.net/problem/13904
#
# Approach
# - 과제를 마감일 기준으로 정렬한 뒤, 선택한 점수만 최소 힙으로 관리한다.
# - 현재 마감일까지 할 수 있는 과제 수를 넘기면 가장 낮은 점수를 버린다.
#
# Review
# - 각 시점까지 유지할 최적 과제 집합을 관리하는 그리디 + 힙 문제다.

N = int(input())
work = [tuple(map(int, input().split())) for _ in range(N)]

work.sort()

hq = []
for d, w in work:
    heapq.heappush(hq, w)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))
