# Section04-2
# 문자열, 문자열 연산, 슬라이싱


str1 = "I am boy!"
str2 = 'Nice man'
str3 = str()

print(len(str1), len(str2), len(str3))

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab \t Tab\t"
print(escape_str2)

# Raw string

raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r"\\a\\a"
print(raw_s2)

# 멀티라인
# 다음 줄로 이어짐.
multi = \
"""
문자열

멀티라인 

test
"""
print(multi)

# 문자열 연산

str_o1 = '*'
str_o2 = 'abc'
str_o3 = 'def'
str_o4 = 'niceman'

print(str_o1 * 100)
print(str_o2 + str_o3)
print('a' in str_o4) # in: a라는 문자가 str_04에 포함되어 있는 지 묻는 함수.
print('z' not in str_o4) # not in : 포함되어 있지 않은 지 판별.