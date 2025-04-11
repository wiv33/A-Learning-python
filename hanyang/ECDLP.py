import numpy as np
import matplotlib.pyplot as plt

def elliptic_curve(x, a, b):
    return np.sqrt(x**3 + a*x + b)

def plot_curve_and_points(a, b, R_x):
    x = np.linspace(-10, 10, 1000)
    y = elliptic_curve(x, a, b)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label="y = sqrt(x^3 + ax + b)", color='blue')
    plt.plot(x, -y, color='blue')  # 반대쪽 곡선

    # R과 -R 계산
    try:
        R_y = elliptic_curve(R_x, a, b)
    except Exception as e:
        print(f"Error computing R: {e}")
        return

    plt.scatter(R_x, R_y, color='red', label='R')
    plt.scatter(R_x, -R_y, color='green', label='-R')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    plt.title(f"Elliptic Curve: y^2 = x^3 + {a}x + {b}")
    plt.legend()
    plt.grid(True)
    plt.show()

# 예시: a, b 변경하면서 R_x를 중심으로 R, -R 보기
plot_curve_and_points(a=-1, b=1, R_x=2)
