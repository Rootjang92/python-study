# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본 출력
print('변수, 문자열, 숫자 다 넣을 수 있음.')
print("큰 따옴표도 가능")
print("""큰 따옴표 3개도 가능""")

print()


# Separator 옵션
# 사이값 문자열 하나로 합쳐줌.
print('T', 'E', 'S', 'T', sep='')
print('2020', '12', '30', sep='-')
print('nice', 'google.com', sep='@')

# end 옵션
# 끝 부분을 end 옵션에 따라 처리.

print('Welcome To', end='')
print(' the black parade', end='')
print(' piano notes')
print('test')


# format 옵션
print('{} and {}'.format('Apple', 'banana'))
print("{0} or {1} or {0}".format('Mac', 'Windows')) # 숫자 매핑
print("{a} and {b}".format(a='You', b='Me'))

print("%s's favorite number is %d or %f" % ('Kim', 5, 5.5)) # %s = 문자, %d = 정수, %f = 실수

print("Test1: %5d, Price: %4.2f" %(775,6345.234))

print("Test1: {0: 5d}, Price: {1: 4.2f}".format(775,2352.3424))

print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=772, b=2352.1243))


# escape

print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n') #\n 개행문자.
print('\t\t\ttest') # \t 들여쓰기.