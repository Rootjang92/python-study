# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this
import sys

# 파이썬 기본 인코딩
print(sys.stdin.encoding) # utf-8
print(sys.stdout.encoding) # utf-8

# 출력문
print('My name is Jang')

# 변수 선언
myName = 'Jang'


# 조건문

if myName == 'Jang':
    print('OK!')

# 반복문
# 구구단

for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)


# 변수 선언 (한글)

이름 = "장근호"

# 출력
print(이름)


# 함수 선언

def greeting():
    print("Hello, Nice to meet you")

greeting()

# 클래스
class Cookie:
    pass

# 객체 생성
cookie = Cookie()

print(id(cookie))
print(dir(cookie))