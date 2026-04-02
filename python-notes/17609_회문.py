import sys

input = sys.stdin.readline

# Problem
# 17609 회문
# https://www.acmicpc.net/problem/17609
#
# Approach
# - 양 끝에서 투 포인터로 회문 여부를 확인한다.
# - 처음 문자가 어긋난 지점에서 왼쪽을 한 번 건너뛴 경우와 오른쪽을 한 번 건너뛴 경우를 각각 검사한다.
# - 둘 중 하나라도 회문이면 유사회문, 둘 다 아니면 일반 문자열이다.
#
# Review
# - 삭제를 실제로 수행하기보다 구간만 조정해서 회문 여부를 확인하는 편이 단순하다.
# - 삭제 기회가 1번뿐이라는 조건 덕분에 분기는 두 경우만 보면 된다.


def is_palindrome(word, left, right):
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


T = int(input())

for _ in range(T):
    word = input().strip()
    ans = 0
    left, right = 0, len(word) - 1

    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
            continue

        if is_palindrome(word, left + 1, right) or is_palindrome(word, left, right - 1):
            ans = 1
        else:
            ans = 2
        break

    print(ans)
