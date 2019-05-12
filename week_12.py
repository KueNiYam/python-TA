# 반복 구조를 사용하면
for x in range(5):
    print('환엽합니다.')

# for 문
for name in ['철수', '영희', '길동', '유신']:
    print('안녕! ' + name)

# range()
for x in range(10):
    sum = sum + x
print(sum)

# 문자열 반복
for c in 'abcdef':
    print(c, end=' ')

# 실습: 정수들의 합
sum = 0

limit = int(input('어디까지 계산할까요: '))
for i in range(1, limit+1):
    sum += i

print('1부터', limit, '까지의 정수의 합=', sum)

# while 문
i = 0;
while i < 5:
    print('환영합니다.')
    i = i + 1
print('반복이 종료되었습니다.')

# 실습: 구구단 출력
for i in range(1, 10):
    print('3*i =', 3*i)

# 실습: 배수의 합 계산
sum = 0
number = 1

while number <= 100:
    if number % 3 == 0:
        sum += number
    number += 1
print('1부터 100사이의 모든 3의 배수의 합은 %d입니다. ' % sum)

# 보초값(sentinel) 사용하기
n = 0
sum = 0
score = 0

print('종료하려면 음수를 입력하시오')
while score > 0:
    score = int(input('성적을 입력하시오: '))
    if score > 0:
        sum += score
        n += 1

    if n > 0:
        average = sum / n
        print('성적의 평균은 %f입니다.' % average)

# 중첩루프
for y in range(5):
    for x in range(10):
        print('*', end='')
    print('')

# 예제: 문자열에서 모음 없애기
s = input('문자열을 입력하시오: ')
vowels = "aeiouAEIOU"
result = ""
for letter in s:
    if letter not in vowels:
        result += letter
print(reslut)

# 함수를 작성해 보자
def say_hello(name, msg):
    print('안녕, ', name, '야, ', msg)

# 값을 반환하는 함수
def get_sum(start, end):
    sum = 0
    for i in range(start, end+1):
        sum += i
    return sum

# 실습: 온도 변환 함수
def f_to_c(temp_f):
    temp_c = (5.0 * (temp_f - 32.0)) / 9.0
    return temp_c

temp_f = float(input('화씨온도를 입력하시오:'))

print(f_to_c(temp_f))

# 디폴트 인수(default argument)
def greet(name, msg='별일없죠?'):
    print('안녕', name + ', ' + msg)

# 키워드 인수
def calc(x, y, z):
    return x+y+z

calc(10, 20, 30)
calc(x=10, y=20, z=30)
calc(y=20, x=10, z=30)

# 값에 의한 호출
def modify(s):
    s += 'To You'

msg = 'Happy Birthday'
print('msg=', msg)
modify(msg)
print('msg=', msg) # 바뀌지 않음

# 참조에 의한 호출
def modify(li):
    li += [100, 200]

list = [1, 2, 3, 4, 5]
print(list)
modify(list)
print(list)cate entry)

#모듈 사용

# fibo.py
def fib(n):
    a, b = 0, 1
    while b < n:
        yield b
        a, b = b, a+b

# main.py
import fibo
fibo.fib(1000)
fibo.__name__ # 'fibo'

from fibo import *
fib(500)
