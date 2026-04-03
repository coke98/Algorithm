import sys
import heapq

input = sys.stdin.readline

# Problem
# 1781 컵라면
# https://www.acmicpc.net/problem/1781
#
# Approach
# - 과제를 마감일 기준으로 정렬한 뒤, 선택한 보상만 최소 힙으로 관리한다.
# - 현재 마감일까지 수행 가능한 과제 수를 넘기면 가장 작은 보상을 버린다.
#
# Review
# - 데드라인 순으로 보면서 작은 보상을 제거하는 방식으로 최적 집합을 유지할 수 있다.

N = int(input())
hw = []

for _ in range(N):
    dead, cup = map(int, input().split())
    hw.append((dead, cup))

hw.sort()
cups = []

for dead, cup in hw:
    heapq.heappush(cups, cup)
    if len(cups) > dead:
        heapq.heappop(cups)

print(sum(cups))
