import sys
from itertools import combinations

input = sys.stdin.readline

# Problem
# 15686 치킨 배달
# https://www.acmicpc.net/problem/15686
#
# Approach
# - 치킨집 중 M개를 고르는 모든 조합을 확인한다.
# - 각 조합마다 모든 집에 대해 살아남은 치킨집들과의 맨해튼 거리 최솟값을 구해 합산한다.
# - 모든 조합 중 도시 치킨 거리가 최소인 값을 답으로 선택한다.
#
# Review
# - 격자 탐색처럼 보여도 거리 정의가 이미 주어지면 BFS보다 좌표 거리 계산이 더 직접적일 수 있다.
# - 집과 치킨집 좌표만 따로 분리하면 로직이 훨씬 선명해진다.

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]


def get_chicken_dist(house, opened):
    r, c = house
    return min(abs(r - cr) + abs(c - cc) for cr, cc in opened)


chickens = []
houses = []

for r in range(N):
    for c in range(N):
        if city[r][c] == 2:
            chickens.append((r, c))
        if city[r][c] == 1:
            houses.append((r, c))

min_dist = float("inf")

for opened in combinations(chickens, M):
    dist_sum = 0

    for house in houses:
        dist_sum += get_chicken_dist(house, opened)
        if dist_sum >= min_dist:
            break

    min_dist = min(min_dist, dist_sum)

print(min_dist)
