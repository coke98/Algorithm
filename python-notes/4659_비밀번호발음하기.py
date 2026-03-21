import sys
input = sys.stdin.readline

# Problem
# 4659 비밀번호 발음하기
# https://www.acmicpc.net/problem/4659

VOWELS = set("aeiou")
DOUBLE_OK = set("eo")

# Question
# 허용되는 비밀번호인지 어떻게 판별할 것인가?
# 조건이 3개인데, 각각 따로 함수로 분리하는 게 더 덜 헷갈릴 것 같다.
# 모음 포함 / 모음or자음 3연속 / 같은 글자 연속(ee, oo 예외)로 나눠서 보자.

# Output
# <word> is acceptable.
# <word> is not acceptable.

# Edge Cases / Checks
# min: 길이 1인 문자열
# blank: 모음이 하나도 없는 경우
# bound: 정확히 모음 3연속 / 자음 3연속이 되는 경우
# dup: 같은 글자 2번 연속일 때, ee / oo만 예외
# counter:
# - 모음은 있지만 자음 3연속인 경우
# - 같은 글자가 연속되지만 ee / oo는 통과해야 하는 경우
# - 출력 마지막에 . 이 빠지면 틀림

# Parse
# end가 나오기 전까지 계속 입력을 받는다.

# Model
# has_vowel(word): 모음이 하나라도 있는지
# has_three_seq(word): 모음/자음이 3개 연속되는지
# has_forbidden_double(word): 같은 글자 2개 연속인데 ee, oo 예외가 아닌지

def has_vowel(word):
    return not VOWELS.isdisjoint(word)


def has_three_seq(word):
    prev = word[0]
    count = 0

    for cur in word[1:]:
        if (cur in VOWELS) == (prev in VOWELS):
            count += 1
            if count >= 2:
                return True
        else:
            count = 0
        prev = cur

    return False


def has_forbidden_double(word):
    prev = word[0]

    for cur in word[1:]:
        if cur == prev and cur not in DOUBLE_OK:
            return True
        prev = cur

    return False


def is_acceptable(word):
    if not has_vowel(word):
        return False
    if has_three_seq(word):
        return False
    if has_forbidden_double(word):
        return False
    return True


while True:
    word = input().strip()
    if word == "end":
        break

    if is_acceptable(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")


# Memo
# 몰랐던 점
# - 출력 문자열 마지막 . 도 조건의 일부라서 정확히 맞춰야 한다.
# - (cur in VOWELS) == (prev in VOWELS) 처럼 괄호로 분명히 써야 의도가 맞다.
#
# 틀렸던 점
# - set(a,e,i,o,u)처럼 문자열 따옴표를 빼먹으면 NameError가 난다.
# - input.strip()처럼 함수 호출을 빼먹으면 입력 처리가 틀어진다.
# - 함수 이름만 쓰고 ()로 호출하지 않으면 로직이 완전히 다르게 동작한다.
# - has_vowel에서 True/False를 반대로 반환했었다.
# - ee, oo 예외 처리를 pass로 넘기면 실제 예외 처리가 되지 않는다.
#
# 잘했던 점
# - 조건을 3개 함수로 분리해서 어디서 틀렸는지 보기 쉬웠다.
# - 처음엔 함수명이 길었지만, 나중에 핵심 의미만 남기도록 줄여서 더 읽기 좋아졌다.
#
# next_checklist
# - 파이썬 문법 실수: 문자열 따옴표, 함수 호출 (), input().strip() 확인
# - 출력 포맷 끝까지 다시 보기
# - 조건 예외는 pass가 아니라 조건식 자체를 바꾸는지 확인하기
