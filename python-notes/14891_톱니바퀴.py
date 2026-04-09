import sys

input = sys.stdin.readline

# Problem
# 14891 톱니바퀴
# https://www.acmicpc.net/problem/14891
#
# Approach
# - 톱니바퀴 문자열은 그대로 두고, 각 톱니의 현재 12시 방향 인덱스만 관리한다.
# - 한 톱니를 돌릴 때는 좌우 회전 전파를 먼저 모두 결정한 뒤 한 번에 적용한다.
#
# Review
# - 회전 판단과 실제 회전 적용을 분리해야 비교 기준이 섞이지 않는다.

wheels = []
commands = []

for _ in range(4):
    wheels.append(input().strip())

N = int(input())

for _ in range(N):
    w, d = map(int, input().split())
    commands.append((w - 1, d))

starts = [0] * 4
rotate = [0, 0, 0, 0]


def right_tooth(w):
    return wheels[w][(starts[w] + 2) % 8]


def left_tooth(w):
    return wheels[w][(starts[w] + 6) % 8]


def get_left_rotate(w, d):
    if w - 1 >= 0 and right_tooth(w - 1) != left_tooth(w):
        rotate[w - 1] = -d
        get_left_rotate(w - 1, -d)


def get_right_rotate(w, d):
    if w + 1 < 4 and left_tooth(w + 1) != right_tooth(w):
        rotate[w + 1] = -d
        get_right_rotate(w + 1, -d)


for w, d in commands:
    rotate = [0, 0, 0, 0]
    rotate[w] = d
    get_left_rotate(w, d)
    get_right_rotate(w, d)

    for w, d in enumerate(rotate):
        starts[w] -= d
        starts[w] %= 8

answer = 0

for i in range(4):
    start = starts[i]
    wheel = wheels[i]

    if wheel[start] == "1":
        answer += 2 ** i

print(answer)
