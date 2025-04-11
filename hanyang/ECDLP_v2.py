import matplotlib.pyplot as plt

# 유한체 소수 p
p = 20408

# 타원 곡선 계수
a = 612312112
b = 30634634626


# 타원 곡선 y^2 = x^3 + ax + b mod p 위의 모든 유효한 점 구하기
def generate_points(a, b, p):
    points = []
    for x in range(p):
        rhs = (x**3 + a*x + b) % p
        for y in range(p):
            if (y*y) % p == rhs:
                points.append((x, y))
    return points

# 모듈러 역원 (Extended Euclidean Algorithm)
def inverse_mod(k, p):
    if k == 0:
        raise ZeroDivisionError('division by zero')
    return pow(k, -1, p)

# 타원 곡선 위의 점 덧셈
def add_points(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:
        return None  # 무한원점 (덧셈 항등원)

    if P == Q:
        # 점 자기 자신과의 덧셈 (탄젠트)
        m = ((3 * x1**2 + a) * inverse_mod(2 * y1, p)) % p
    else:
        # 일반 점 덧셈
        m = ((y2 - y1) * inverse_mod(x2 - x1, p)) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p

    return (x3, y3)

# 점 음수 구하기
def negate_point(P, p):
    x, y = P
    return (x, (-y) % p)

# 시각화
def plot_curve_and_points(points, P, Q, R, R_neg, a, b, p):
    xs, ys = zip(*points)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

    # ------------------------
    # 왼쪽: 유한체 위의 곡선 점들
    # ------------------------
    ax1.scatter(xs, ys, s=15, color='lightgray', label='Finite Field Points')

    if P: ax1.scatter(*P, color='red', label='P')
    if Q: ax1.scatter(*Q, color='blue', label='Q')
    if R: ax1.scatter(*R, color='green', label='R = P + Q')
    if R_neg: ax1.scatter(*R_neg, color='orange', label='-R')

    ax1.set_title(f"Elliptic Curve over F_p (mod {p})")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.grid(True)
    ax1.legend()

    # ------------------------
    # 오른쪽: 실수 위의 곡선
    # ------------------------
    x_real = [x / 100 for x in range(-500, 500)]
    y_real_pos, y_real_neg, x_vals = [], [], []

    for x in x_real:
        val = x**3 + a*x + b
        if val >= 0:
            y = val**0.5
            x_vals.append(x)
            y_real_pos.append(y)
            y_real_neg.append(-y)

    ax2.plot(x_vals, y_real_pos, color='gray', linestyle='dotted', label='Real Curve (+y)')
    ax2.plot(x_vals, y_real_neg, color='gray', linestyle='dotted', label='Real Curve (-y)')

    ax2.set_title(f"Elliptic Curve over ℝ: y² = x³ + {a}x + {b}")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.grid(True)
    ax2.legend()

    plt.tight_layout()
    plt.show()

# 실행
points = generate_points(a, b, p)

# 예제 점 선택
P = (3, 6)
Q = (80, 10)
R = add_points(P, Q, a, p)
R_neg = negate_point(R, p) if R else None

# 시각화
plot_curve_and_points(points, P, Q, R, R_neg, a, b, p)

# 결과 출력
print(f"P = {P}")
print(f"Q = {Q}")
print(f"R = P + Q = {R}")
print(f"-R = {R_neg}")
