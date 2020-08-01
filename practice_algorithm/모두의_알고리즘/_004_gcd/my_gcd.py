# 최대공약수 greatest common divisor
# 두 수의 약수 중
# 공통된 것을 찾고,
# 그 값 중 최댓값인 것

print(__name__)


def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1
