import time

import numpy as np


"""Numpy - Python 라이브러리이지만 코어는 C로 구현되어 있다.
        :속도가 빠름
    
    라이브러리 구현되어 있는 함수들을 활용해 짧고 간결한 코드 작성 가능
    효율적인 메모리 관리가 가능하도록 구현되어 있다.
    
    내부의 자료구조가 다르다.
        - numpy array는 데이터를 스택과 같은 영역에 주소가 아닌,
        실제 데이터를 연속적으로 저장한다.
        - type을 명시하여 바이트 크기가 일정하다.
        - stride 로 데이터를 읽을 순서를 지정한다.
        ** ex) x [stride(2,1)]  y = x.T [stride(1,2)]
        
        - python list는 포인터 배열로 주소 값이 저장되어 있다.
        numpy array 보다 한 단계 더 거쳐야한다. (주소에 가서 데이터를 확인)
        
"""

class Timer(object):
    """실행 속도 체크 클래스"""
    def __init__(self, name=None):
        self.name = name

    def __enter__(self):
        self.tstart = time.time()

    def __exit__(self, type, val, traceback):
        if self.name:
            print('[%s]' % self.name)
        print('Elapsed: %s' % (time.time() - self.tstart))



rows = 1000
cols = 1000

sample2DArray = np.random.rand(rows, cols)
sample2DList = sample2DArray.tolist()

print(sample2DArray)
print(sample2DList)

with Timer("모든 원소의 합 구하기"):
    sum = 0

    for list in sample2DList:
        for e in list:
            sum += e

with Timer("모든 원소의 1 더하기"):
    sample2DList2 = []

    for list in sample2DList:
        tempList = []
        for e in list:
            tempList.append(e + 1)

    sample2DList2.append(tempList)


print("===============================================")


with Timer("Numpy - 모든 원소의 합"):
    sum = np.sum(sample2DArray)

with Timer("Numpy - 모든 원소에 1 더하기"):
    sample2DArray2 = sample2DArray + 1

