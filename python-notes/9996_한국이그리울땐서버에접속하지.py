import sys
input = sys.stdin.readline

# Problem
# 9996 한국이 그리울 땐 서버에 접속하지
# https://www.acmicpc.net/problem/9996

# Question
# 패턴에 맞는지 아닌지 어떻게 확인할것인가?
# 패턴에 있는 앞뒤 문자들은 문자인가 문자열인가? 문자열임.

# Output
# "DA","NE"

# Edge Cases / Checks
# min, max, blank: N 1, 100일때: 가능, 문자열 길이가 100: 가능, 빈 문자열로 치환하는 경우 가능
# bound: 중복되는 경우 길이 체크시 경계 범위 재확인
# dup: 패턴에서 중복되는 길이가 있을 경우: len(start) + len(end)만큼 큰지 확인하기
# COUNTER:
# - 앞은 맞는데 뒤는 틀린 경우
# - 뒤는 맞는데 앞은 틀린 경우
# - 길이가 부족해서 겉보기엔 비슷해도 안 되는 경우

# Parse
N = int(input())  # (1 ≤ N ≤ 100)
pattern = input().strip()  # len <= 100, 소문자문자열 + '*' + 소문자문자열
cases = [input().strip() for _ in range(N)]  # len <= 100, 소문자문자열

# Model
start, end = pattern.split("*")


# Solve
def is_pattern(case):
    if len(case) < len(start) + len(end):
        return "NE"
    if not case.startswith(start):
        return "NE"
    if not case.endswith(end):
        return "NE"
    return "DA"


for case in cases:
    print(is_pattern(case))
