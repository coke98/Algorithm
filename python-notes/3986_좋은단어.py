import sys
input = sys.stdin.readline

# Problem
# 3986 좋은 단어
# https://www.acmicpc.net/problem/3986
#
# Approach
# - 인접한 같은 문자가 나오면 제거하는 과정을 스택으로 모델링한다.
# - 모든 문자를 처리한 뒤 스택이 비어 있으면 좋은 단어로 판단한다.
#
# Review
# - 문자열 직접 삭제보다 스택 모델이 구현과 복잡도 측면에서 적절했다.
# - 유사 문제에서는 삭제/상쇄 패턴을 먼저 확인할 것.

N = int(input())
words = [input().strip() for _ in range(N)]


def is_good_word(word):
    st = []
    for ch in word:
        if st and st[-1] == ch:
            st.pop()
        else:
            st.append(ch)
    return not st


ans = 0
for word in words:
    if is_good_word(word):
        ans += 1

print(ans)
