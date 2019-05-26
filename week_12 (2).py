# 실습: 정수들의 합
def sum_int(n: int) -> int:
    return sum(range(0,n+1))

print(sum_int(100))

# 실습: 구구단 출력
i = 1
while i <= 9:
    print(3 * i, end=('\n' if i == 9 else ' ' ))
    i += 1

# 실습: 배수의 합 계산
sum_three_multiple = sum(range(0, 100, 3))
print(sum_three_multiple)

# 예제: 문자열에서 모음 없애기
VOWELS = 'aeiouAEIOU'
def remove_vowels(string: str) -> str:
    return ''.join(letter for letter in string if letter not in VOWELS)

print(remove_vowels('kkkoommm'))