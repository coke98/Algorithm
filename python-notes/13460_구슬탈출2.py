import sys
from collections import deque, defaultdict

input = sys.stdin.readline

# Problem
# 13460 구슬 탈출 2
# https://www.acmicpc.net/problem/13460
#
# Approach
# - 상태를 빨간 구슬 위치와 파란 구슬 위치로 두고 BFS를 한다.
# - 한 방향으로 기울일 때 두 구슬을 각각 끝까지 굴린 뒤 결과 상태를 만든다.
#
# Review
# - 이 문제는 BFS 자체보다 구슬 이동 시뮬레이션과 겹침 조정이 핵심이다.

drs, dcs = [-1, 0, 0, 1], [0, -1, 1, 0]


def move(sr, sc, dr, dc):
    nr, nc = sr, sc
    d = 0

    while board[nr + dr][nc + dc] != "#":
        nr, nc = nr + dr, nc + dc
        d += 1
        if board[nr][nc] == "O":
            d = -1
            break

    return nr, nc, d


def bfs(R, B):
    rsr, rsc = R
    bsr, bsc = B
    q = deque()
    q.append((rsr, rsc, bsr, bsc))
    cost = defaultdict(int)
    cost[(rsr, rsc, bsr, bsc)] = 1

    while q:
        rr, rc, br, bc = q.popleft()

        if cost[(rr, rc, br, bc)] > 10:
            continue

        for dr, dc in zip(drs, dcs):
            nrr, nrc, rd = move(rr, rc, dr, dc)
            nbr, nbc, bd = move(br, bc, dr, dc)

            if bd == -1:
                continue

            if rd == -1:
                return cost[(rr, rc, br, bc)]

            if (nrr, nrc) == (nbr, nbc):
                if bd < rd:
                    nrr, nrc = nrr - dr, nrc - dc
                else:
                    nbr, nbc = nbr - dr, nbc - dc

            if 0 < cost[(nrr, nrc, nbr, nbc)] <= cost[(rr, rc, br, bc)] + 1:
                continue

            cost[(nrr, nrc, nbr, nbc)] = cost[(rr, rc, br, bc)] + 1
            q.append((nrr, nrc, nbr, nbc))

    return -1


N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

R = None
B = None

for r in range(N):
    for c in range(M):
        if board[r][c] == "R":
            R = (r, c)
        if board[r][c] == "B":
            B = (r, c)

print(bfs(R, B))
