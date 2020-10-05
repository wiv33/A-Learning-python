Pandas
=

    세 가지의 데이터 구조
    
    Series
        1차원 배열의 형태
    
    DataFrame
        2차원 데이터 구조
        
    Panel
        3차원 데이터 구조 (데이터프레임의 모음)


---

## create

```python
import pandas as pd
pd.Series(data, index, dtype, copy)

pd.DataFrame(data, index, colums, dtype, copy)

```

## 평균, 표준편차 등 다양한 수치 값 확인
```python
import pandas as pd
data_frame = pd.DataFrame([['a', 7000], ['b', 6000], ['c', 3000]])
data_frame.describe()
```
                     1
    count     3.000000
    mean   5333.333333
    std    2081.665999
    min    3000.000000
    25%    4500.000000
    50%    6000.000000
    75%    6500.000000
    max    7000.000000