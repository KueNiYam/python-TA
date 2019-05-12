# if-else 문
if score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")

# 관계연산자
age = 19
if age >= 19:
    print("마트에서 주류를 구입할 수 있습니다.")
else:
    print("조금 기다리세요!")

# else는 생략 가능
food = '스테이크'
if food == '스테이크':
    print('내가 제일 좋아하는 음식!')
    print(10 * food)

# 실습: 수하물 비용 계산
weight = float(input('짐의 무게는 얼마입니까? '))
if weight > 20:
    print('무거운 짐은 20,000원을 내셔야 합니다.')
else:
    print('짐에대한 수수료는 없습니다.')

# 실습: 짝수 홀수 구분하기
integer = int(input('정수를 입력하시오: '))
if integer & 1:
    print('입력된 정수는 홀수입니다.')
else:
    print('입력된 정수는 짝수입니다.')

# 실습: 둘 중 큰 수 찾기
first = int(input('첫 번째 정수: '))
second = int(input('두 번째 정쉬: '))
if first > second:
    print(first)
elif first < second:
    pirnt(first)
else:
    pass

# 실습: 할인된 물건 가격 계산
total_sales = int(input('구입 금액을 입력하시오:'))
if total_sales > 100000:
    discount = total_sales * 0.05
    sales = total_sales - discount
print('지불 금액은', sales, '입니다.')

# 논리연산자
age = 20
height = 180
if age >= 10 and height >= 165:
    print('놀이 기구를 탈 수 있습니다.')
else:
    print('놀이 기구를 탈 수 없습니다.')

# 연속적인 if-else 문 (if, elif, else)
score = int(input('성적을 입력하시오: '))

if score >= 90:
    print('학점 A')
elif score >= 80:
    print('학점 B')
elif score >= 70:
    print('학점 C')
elif score >= 60:
    print('학점 D')
else:
    print('학점 F')

# 실습: 음수, 0, 양수 구분하기
number = int(input('정수를 입력하시오: '))
if number < 0:
    print('입력된 정수는 음수입니다.')
elif number == 0:
    print('입력된 정수는 0입니다.')
else:
    print('입력된 정수는 양수입니다.')

# 중첩 if-else 문
appleQuality = input('사과의 상태를 입력하시오: ')
applePrice = int(input('사과 1개의 가격을 입력하시오: '))
if appleQuality == '신선':
    if applePrice < 1000:
        print('10개를 산다')
    else:
        print('5개를 산다')
else:
    print('사과를 사지 않는다.')

# HW#3: BMI 따른 비만도 계산
weight = float(input('몸무게(킬로그램): '))
height = float(input('키(미터): '))
BMI = weight / (height ** 2)

if BMI >= 30:
    print('비만입니다.')
elif BMI >= 25:
    print('과체중입니다.')
elif BMI >= 29:
    print('정상입니다.')
