import sys

input = sys.stdin.readline

# Problem
# 14499 주사위 굴리기
# https://www.acmicpc.net/problem/14499
#
# Approach
# - 주사위 상태를 십자 형태 배열로 관리하고, 방향별 회전 함수를 따로 둔다.
# - 이동 가능한 경우에만 좌표 이동, 회전, 바닥/칸 복사, 윗면 출력을 수행한다.
#
# Review
# - 주사위 회전과 칸 숫자 복사 규칙을 분리해서 구현하면 흐름이 덜 꼬인다.

N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = [[0] * 3 for _ in range(4)]


def west():
    tmp = dice[1][0]
    dice[1] = dice[1][1:] + dice[-1][1:2]
    dice[-1][1] = tmp


def east():
    tmp = dice[1][-1]
    dice[1] = dice[-1][1:2] + dice[1][:2]
    dice[-1][1] = tmp


def south():
    prev = dice[-1][1]
    for i in range(4):
        cur = dice[i][1]
        dice[i][1] = prev
        prev = cur


def north():
    prev = dice[0][1]
    for i in range(4):
        cur = dice[3 - i][1]
        dice[3 - i][1] = prev
        prev = cur


def top():
    return dice[1][1]


def bottom():
    return dice[-1][1]


def write(num):
    dice[-1][1] = num


move = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]

for cmd in commands:
    dr, dc = move[cmd]
    nr, nc = r + dr, c + dc

    if not (0 <= nr < N and 0 <= nc < M):
        continue

    r, c = nr, nc

    if cmd == 1:
        east()
    if cmd == 2:
        west()
    if cmd == 3:
        north()
    if cmd == 4:
        south()

    if board[r][c] != 0:
        write(board[r][c])
        board[r][c] = 0
    else:
        board[r][c] = bottom()

    print(top())
