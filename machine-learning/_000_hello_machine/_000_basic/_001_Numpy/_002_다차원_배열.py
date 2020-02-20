"""
다차원 배열의 데이터 타입은
    '모든 원소의 데이터 타입이 같아야한다.'
"""
import numpy as np

"""bool
    직접 원소를 입력해서 다차원 배열 생성할 때
    np.array()
"""

boolArray = np.array([True, False, True, True])

print(boolArray.dtype)

"""number
    정수형, 부호없는 정수형, 실수형 복소수형
    '정수형의 default data type은 int64'
    운영체제에 따라 다르다.
"""

intArray = np.array([[1,2], [3,4]])

print(intArray)
print(intArray.dtype)
# int32


uintArray = np.array([[1,2],[3,4]], dtype='uint64')

print(uintArray)
print(uintArray.dtype)
# uint32


"""실수형
    default data type: float64
"""

floatArray = np.array([[1,2.2, 3.5], [4,5.2,10.2]], dtype='float16')
print(floatArray)