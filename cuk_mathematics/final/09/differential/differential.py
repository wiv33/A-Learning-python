"""
미분
기울기: 크기가 서로 다른 삼각형이 있을 때 크기를 표준화 하면 됨.

밑변의 길이를 1로 맞추고, 맞춰진 높이를 기울기라고 한다.

접선의 기울기는 순간 변화율로 표현할 수 있다.

무한소
: 무한히 작은 변화값을 나타내는 값 == 미분소
: dx
x는 x인데 사이즈가 0에 무한히 가까워지는 x 다.
y도 무한히 0에 가까워 진다.
둘 다 0에 무한히 가까워지는 것이기 때문에
dy/dx 로 표시할 수 있다.

상대성 이론에 의하면 블랙홀 중심부에 가까워지면 시간이 느려지기 때문에
도달할 수는 없는 개념과 같음

dx != 0, dx == 0에 아주 가깝지만 0은 아님.

함수 그래프
: x^2 - x - y - 2 = 0

# 도함수, derivative
:함수를 미분하여 얻은 함수

## 미분 계수를 도함수로 만들고, 도함수를 구하는 것을 `미분한다`고 표현한다.

# 시간에 대한 미분
: dx/dt = v, 시간에 따른 속도에 변화를 나타낸 그래프가 미분임.
: 미분을 계산하는 것까지 연습 필요.

선형성
: [f(x) + g(x)]‘ =

# 여러가지 함수의 미분 공식
1. 숫자는 미분하면 0이 된다.
- c‘ = 0, 3‘ = 0
[x^n]‘ = nx^n-1
[e^x]‘ = e^x : 지수함수를 미분하면 자기 자신이 나옴.
[sin x]‘ = cos x
[cos x]‘ = -sin x

# 다항식의 미분 공식: 중요함.
x^n = n * x ^ n - 1 : 미분항 공식
x^3 = 3 * x ^ 2
x^1 = 1

# 다음 함수를 미분하시오.
1. f(x) = x
=> 1

2. f(x) = x^2
=> f‘(x) = 2x

3. f(x) = x^4
=> f‘(x) = 4x^3

4. f(x) = 6
=> f‘(x) = 0

5. f(x) = 2x
=> f‘(x) =



# 다음 함수를 미분하시오.

1. y = x + 3
=> y‘ = 1

2. y = 3x^2 - 2
=> y‘ = 3 * 2x = 6x

3. f(x) = 3x^3 + 2x + 1
=> f‘(x) = 3 * 3x^2 + 2 = 9x^2

4. g(x) = e^x + 1
=> g‘(x) = e^x

5. f(t) = -2cost + t
=> f‘(t) = -2(-sin t) + 1 = 2 sin t + 1

6. g(x) = sin s + 3 s^2 + 8s - 1
=> g‘(s) = cos s + 3 * 2s + 8 = cos s ???

7. y = 3e^x + 2x^2 - 2 sin x + e
=> y‘ = 3e^x + 2 * 2x - 2cos x = 3e^x + 4x - 2cos x


# 다음 함수를 미분하시오.
: 선형성을 쓸 수 없음

1. f(x) = x^2e^x
=> f‘(x) = 2x * e^x + x^2
=> e^x(2x + x^2)
=> xe^x(2+x)

2. y = sin x / x^2
=> y‘ = (cos x)x^2 - (sin x) * 2x / x^4
=> x^2 cos x - 2x sin x / x^4
=> x cos x - 2 sin x / x^3
& sin x, cos x는 나누지 않는다. (다른 것.)

# 함수 y = f(x) = 2x^3 + 2x^2 - 7에 대하여 다음을 구하시오.
1. d^2y/dx^2 :: 두 번 미분하라.
=> y‘ = dy/dx = 6x^2 + 4x
=> 6 * 2x + 4 * 1 = 12x + 4

2. d^3y/dx^3 :: 세 번 미분하라.
=> 6 * 2x + 4 * 1 = 12x + 4
=> 12


# 편미분, partial differentiation
:다변수함수를 하나의 변수에만 주목하고 나머지 변수는 상수로 보고 미분

# 편도함수, partial derivative
: 다변수함수를 편미분하여 얻은 함수.

편미분을 하면 모눈 종이에 따라서 단면이 나타남.
∂z / ∂x == y를 편미분
∂z / ∂y == x를 편미분
y가 해당 지점인 x선을 따라서 편미분 한 것(단면)

# 벡터의 스칼라 편미분.
# 벡터를 벡터로 미분



# 다변수함수의 행렬 미분
: 다변수함수 f(x1, x2, x3, …, xn)의 행렬이 있을 때, 각 변수에 맞는 편미분을 하는 것 (계산 횟수가 많을 뿐 어렵지 않음)


"""

# TODO 다변수함수의 행렬 미분 계산식 만들어야 함.