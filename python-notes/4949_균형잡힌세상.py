import sys
input = sys.stdin.readline

# Problem
# 4949 균형잡힌 세상
# https://www.acmicpc.net/problem/4949
#
# Approach
# - 열린 괄호는 스택에 넣고, 닫는 괄호가 나오면 스택 top과 짝이 맞는지 확인한다.
# - 괄호 외 문자는 무시하고, 끝까지 처리한 뒤 스택이 비어 있으면 균형잡힌 문자열로 판단한다.
#
# Review
# - 입력 문자열 전체를 다루는 문제라 종료 조건 처리에서 문자열 보존이 중요했다.
# - 유사 문제에서는 스택과 입력 처리 방식을 함께 확인할 것.


def is_balanced(line):
    st = []

    for ch in line:
        if ch not in "()[]":
            continue

        if ch in "([":
            st.append(ch)

        if ch in ")]":
            if not st:
                return False
            if ch == ")" and st[-1] != "(":
                return False
            if ch == "]" and st[-1] != "[":
                return False
            st.pop()

    return not st


while True:
    line = input().rstrip("\n")
    if line == ".":
        break

    print("yes" if is_balanced(line) else "no")
