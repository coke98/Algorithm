import sys
import heapq

input = sys.stdin.readline

# Problem
# 1715 카드 정렬하기
# https://www.acmicpc.net/problem/1715
#
# Approach
# - 카드 묶음을 최소 힙에 넣고, 가장 작은 두 묶음을 반복해서 합친다.
# - 합친 비용을 누적하고, 새 묶음을 다시 힙에 넣는다.
#
# Review
# - 항상 가장 작은 두 묶음을 먼저 합쳐야 전체 비교 횟수의 합이 최소가 된다.

N = int(input())
decks = []

for _ in range(N):
    heapq.heappush(decks, int(input()))

answer = 0

while len(decks) > 1:
    a = heapq.heappop(decks)
    b = heapq.heappop(decks)
    answer += a + b
    heapq.heappush(decks, a + b)

print(answer)
