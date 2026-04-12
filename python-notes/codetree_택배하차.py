import sys

input = sys.stdin.readline

# Problem
# 코드트리 택배 하차
#
# Approach
# - 현재 방향에서 꺼낼 수 있는 택배를 찾고, 하나 제거할 때마다 남은 택배를 다시 아래로 떨어뜨린다.
# - 접근 가능한 후보가 여러 개면 번호가 가장 작은 택배를 먼저 하차한다.
#
# Review
# - 부분 갱신보다 제거 후 전체 낙하를 다시 구성하는 쪽이 구현이 더 안정적이었다.

N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]
boxes = {}


def down(k, h, w, c, cur_r):
    max_f = 0

    for row in range(cur_r, N):
        for col in range(c, c + w):
            if board[row][col] != 0:
                break
        else:
            max_f = max(max_f, row)
            continue
        break

    for row in range(max_f - h + 1, max_f + 1):
        for col in range(c, c + w):
            board[row][col] = k

    return max_f


for _ in range(M):
    k, h, w, c = map(int, input().split())
    f = down(k, h, w, c - 1, 0)
    boxes[k] = (h, w, c - 1, f)


def pick_box(direction):
    visible = {}

    for row in range(N - 1, -1, -1):
        for col in range(N):
            col = col if direction == 1 else N - 1 - col
            k = board[row][col]
            if k != 0:
                visible[k] = visible.get(k, 0) + 1
                break

    for k in sorted(visible.keys()):
        if visible[k] == boxes[k][0]:
            return k


answer = []
removed = set()
direction = 1

while len(answer) < M:
    k = pick_box(direction)
    answer.append(k)
    removed.add(k)

    board = [[0] * N for _ in range(N)]
    for box_k, info in sorted(boxes.items(), key=lambda x: -x[1][3]):
        if box_k in removed:
            continue
        h, w, c, f = info
        down(box_k, h, w, c, f)

    direction = -1 if direction == 1 else 1

print(*answer, sep="\n")
