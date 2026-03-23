import sys
input = sys.stdin.readline

# Problem
# 2870 수학숙제
# https://www.acmicpc.net/problem/2870
#
# Approach
# - 각 문자열을 순회하면서 숫자만 이어붙여 하나의 숫자 구간을 만든다.
# - 문자를 만나면 지금까지 만든 숫자 구간을 정수로 변환해 저장하고, 마지막에 전체를 정렬한다.
#
# Review
# - 실시간 정렬보다 모든 숫자를 수집한 뒤 정렬하는 방식이 더 단순했다.
# - 숫자 구간 추출은 인덱스 관리보다 문자열 누적이 안정적이었다.

NUMBER = "0123456789"
ans = []


def addnums(word):
    num = ""

    for ch in word:
        if ch in NUMBER:
            num += ch
        else:
            if num != "":
                ans.append(int(num))
            num = ""

    if num != "":
        ans.append(int(num))


N = int(input())
words = [input().rstrip("\n") for _ in range(N)]

for word in words:
    addnums(word)

for num in sorted(ans):
    print(num)
