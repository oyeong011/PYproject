# 정수형
a=1000
print(a)
a=-7
print(a)
a=0
print(a)
# 실수형
a = 157.93
print(a)
a = -1837.2
print(a)
a = 5.
print(a)
a = -.7
print(a)
# 지수표현방식 유효숫자e지수 = 유효숫자 x 10지수
# 1,000,000,000의 지수 표현
a = 1e9
print(a)
# 752.5
a = 75.25e1
print(a)
# 3.954
a = 3954e-3
print(a)
#실수형 추가
a = 0.3 + 0.6# 0.899999999999999999
print(a)
if a==0.9:
    print(True)
else:
    print(False)
# round(a,b) b번째에서 반올림
a = 0.3 + 0.6
print(round(a,4))

a = 7
b = 3
# 나누기
print(a / b)
# 나머지
print(a % b)
# 몫
print(a // b)
# 거듭제곱
print(a ** b)
#제곱근
print(a // 0.5)


# 리스트 자료형
a = [1,2, 3, 4,5,6,7,8,9]
print(a)
# 4번째 요소 출력
print(a[3])
# 크기가 N이고 모든값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n
print(a)

# 리스트 인덱싱, 슬라이싱
a = [1,2,3,4,5,6,7,8,9]
print(a[7])
# 뒤에서 첫번째
print(a[-1])
print(a[-3])
a[3] = 7
print(a)
a = [1,2,3,4,5,6,7,8,9]
print(a[3])
# 두번쨰 원소부터 네번째 원소까지
print(a[1:4])

# 리스트 컴프리헨션
# 0부터 9까지의 수를 포함하는 리스트
array = [i for i in range(10)]
print(array)
# 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)
# 1부터 9까지의 수들의 제곱값을 포함하는 리스트
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# 리스트 컴프리 헨션
# NxM 크기의 2차원 리스트 초기화

n = 3
m = 4
array = [[0] * m for _ in range(n)]
print(array)

array[2][1] = 5
print(array)

# 리스트 관련 메서드
# append sort reverse insert count remove

# 문자열 자료형

# 튜플 자료형

a = (1,2,3,4,5,6,7,8,9)

# 딕셔너리 자료형

data = {}
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
key_list = data.keys()
value_list = data.values()

# 집합자료형
data = set([1,1,2,3,4,4,5])
data = {}