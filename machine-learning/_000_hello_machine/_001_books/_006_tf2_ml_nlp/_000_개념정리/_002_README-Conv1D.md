# Conv1D

## conv1d filtering
    가로 방향으로만 옮겨가면서 입력값에 대해 합성곱을 수행한다.
    연산 결과들이 모여서 최종 출력 값이 나오며,
    출력 값은 1차원 벡터가 된다.
   
- Flatten 느낌 


    Dense와 다른 점은 합성곱 연산을 수행하는 필터와 관련된 부분이 추가된 점.
    합성곱은 필터의 크기를 필요로 하나, Conv1D는 필터의 높이(high)는 필요하지 않다.
    
```python
input = (5,10)
kernel_size = 2
filter = 10
# ---
output = (1, 4, 10)
```
    
Q. 필터의 크기가 5일 경우 1, 5, 10일까?


---
tf.keras.layers.Conv1D().__init__()

filters
-
    필터의 개수
    정수형으로 지정
    **출력의 차원 수를 나타냄**
    
kernel_size
-
    필터의 크기
    정수 or 정수 리스트 or 튜플
    합성곱이 적용되는 윈도우의 길이를 나타냄
    
strides
-
    적용할 스트라이드 값
    정수 or 정수 리스트 or 튜플
    1이 아닌 값을 지정할 경우 dilation_rate는 1 이외의 값을 지정하지 못한다.
    
padding
-
    값 : "VALID", "SAME"

data_format
-
    데이터의 표현 방법 선택 설정
    "channel_last", "channel_first"
    ex) 
        channel_last
            (batch, length, channels)
        
        channel_fisrt
            (batch, channels, length)
            
dilation_rate
-
    dilation 합성곱 사용 시 적용할 값
    정수 or 정수 리스트 or 튜플
    1이 아닌 값을 지정하면 strides 값은 1 이외의 값을 지정하지 못한다.
    
activation
-
    활성화 함수
    
use_bias
-
    편향(b)을 사용할지 여부
    값: Boolean
    
kernel_initializer
-
    가중치(W) 초기화 함수
    
bias_initializer
-
    편향 초기화 함수
    
kernel_regularizer
-
    가중치 정규화 방법
    
bias_regularizer
-
    편향 정규화 방법
    
activity_regularizer
-
    출력 값 정규화 방법
    
kernel_constraint
-
    optimizer에 의해 업데이트된 후 가중치에 적용되는 부가적인 제약 함수
    ex) norm constraint, value constarint
    
bias_constraint
-
    optimizer에 의해 업데이트된 후 편향에 적용되는 부가적인 제약 함수
    ex) norm constraint, value constraint