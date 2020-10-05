# MaxPool1D

    피처 맵에 대해 최댓값만 추출하는 방식

## average pooling
    
    피처 맵에 대해 전체 값들의 평균을 추출하는 방식


# Pooling

* 크기를 줄이거나 주요한 특징을 추출하기 위해 합성곱 이후 적용되는 기법

* 한 방향으로만 풀링이 진행된다.
    

```python
max_pool = tf.keras.layers.MaxPool1D()
max_pool.apply(input)

max_pool = tf.keras.layers.MaxPool1D()(input)
```

---

tf.keras.layers.MaxPool1D().__init__()

pool_size
-
    풀링을 적용할 필터의 크기
    type: 정수

strides
-
    적용할 stride 값
    type: 정수 or None
    
padding
-
    패딩 방법을 지정
    "valid" or "same"

date_format
- 
    데이터의 표현 방법을 선택
    "channel_last", "channel_first"
        ex) 
            channel_last
                (batch, length, channels)
            
            channel_fisrt
                (batch, channels, length)
