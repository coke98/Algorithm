import sys

input = sys.stdin.readline

# Problem
# 14503 로봇 청소기
# https://www.acmicpc.net/problem/14503
#
# Approach
# - 문제에서 주어진 로봇의 동작 순서를 그대로 시뮬레이션한다.
# - 현재 위치를 청소한 뒤, 현재 방향 기준 왼쪽부터 4방향을 차례대로 확인한다.
# - 청소되지 않은 빈칸이 있으면 그 방향으로 회전 후 전진한다.
# - 4방향 모두 갈 수 없으면 방향을 유지한 채 후진하고, 뒤가 벽이면 종료한다.
#
# Review
# - 방향 회전 순서만 정확히 맞추면 본문 절차대로 구현할 수 있다.
# - `for-else`를 사용해 4방향 탐색 실패와 후진 분기를 자연스럽게 연결했다.

N, M = map(int, input().split())
r, c, d = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
answer = 0

while True:
    if matrix[r][c] == 0:
        matrix[r][c] = 2
        answer += 1

    for i in range(4):
        dr, dc = move[(d - (i + 1)) % 4]
        nr, nc = r + dr, c + dc

        if matrix[nr][nc] == 0:
            r, c = nr, nc
            d = (d - (i + 1)) % 4
            break
    else:
        dr, dc = move[d]
        nr, nc = r - dr, c - dc

        if matrix[nr][nc] != 1:
            r, c = nr, nc
        else:
            break

print(answer)
