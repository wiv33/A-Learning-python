"""
a와 b는 b와 a를 b로 나눈 나머지의 최대공약수와 같다.
gcd(a, b) = gcd(b, a % b)

gcd(60, 24) = gcd(24, 60 % 24)
gcd(24, 12) = gcd(24, 24 % 12)
gcd(12, 0) = 12
"""


def gcd_euclid(a, b):
    return a if b == 0 else gcd_euclid(b, a % b)
