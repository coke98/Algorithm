import sys
import heapq

input = sys.stdin.readline

# Problem
# 11000 강의실 배정
# https://www.acmicpc.net/problem/11000
#
# Approach
# - 강의를 시작 시간 기준으로 정렬하고, 사용 중인 강의실 종료 시간을 최소 힙으로 관리한다.
# - 가장 빨리 끝나는 강의실을 재사용할 수 있으면 꺼내고, 현재 강의 종료 시간을 넣는다.
#
# Review
# - 답을 직접 세기보다 현재 사용 중인 강의실 집합을 힙으로 유지하고, 마지막 힙 크기를 쓰는 편이 안전하다.

N = int(input())
courses = sorted(tuple(map(int, input().split())) for _ in range(N))

ends = []

for start, end in courses:
    if ends and ends[0] <= start:
        heapq.heappop(ends)
    heapq.heappush(ends, end)

print(len(ends))
