# 문자열에서 단어 분리하기

s = 'Never put off till tomorrow what you can do today.'
print(s.split())

# HW5
tel_dir = {}
def get_number(tel_dir: dict) -> None:
    name = input('이름: ')
    number = input('전화번호: ')
    tel_dir[name] = number
    
    return

for i in range(0,5):
    get_number(tel_dir)

name = input('누구의 전화번호?: ')
print(tel_dir[name])