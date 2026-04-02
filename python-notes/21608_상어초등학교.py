import sys
input = sys.stdin.readline

# Problem
# 21608 상어 초등학교
# https://www.acmicpc.net/problem/21608
#
# Approach
# - 학생을 입력 순서대로 배치하면서 모든 빈칸의 우선순위를 평가한다.
# - 각 빈칸마다 인접한 좋아하는 학생 수와 인접한 빈칸 수를 세고,
#   좋아하는 학생 수가 가장 큰 칸만 후보로 남긴다.
# - 후보가 여러 개면 빈칸 수, 그다음 행/열 순으로 정렬해 자리를 확정한다.
#
# Review
# - 구현 전에 수도코드로 우선순위 비교 단계를 분리해두는 방식이 유효했다.

N = int(input())

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
matrix = [[0] * N for _ in range(N)]
pref_map = {}

for _ in range(N * N):
    line = list(map(int, input().split()))
    student, prefs = line[0], line[1:]
    pref_map[student] = prefs

    max_pref = 0
    cands = []

    for r in range(N):
        for c in range(N):
            if matrix[r][c] != 0:
                continue

            blank_cnt = 0
            pref_cnt = 0

            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]

                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                nstudent = matrix[nr][nc]
                if nstudent in prefs:
                    pref_cnt += 1
                if nstudent == 0:
                    blank_cnt += 1

            if pref_cnt > max_pref:
                cands = []
                max_pref = pref_cnt

            if pref_cnt == max_pref:
                cands.append((blank_cnt, r, c))

    cands.sort(key=lambda x: (-x[0], x[1], x[2]))
    _, r, c = cands[0]
    matrix[r][c] = student

score_board = [0, 1, 10, 100, 1000]
ans = 0

for r in range(N):
    for c in range(N):
        student = matrix[r][c]
        pref_cnt = 0

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N):
                continue

            nstudent = matrix[nr][nc]
            if nstudent in pref_map[student]:
                pref_cnt += 1

        ans += score_board[pref_cnt]

print(ans)
