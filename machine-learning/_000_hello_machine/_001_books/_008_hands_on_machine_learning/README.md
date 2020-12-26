# Hands on machine learning

## Tensorflow

- 핵심 구조는 넘파이와 비슷하고 `GPU`를 지원한다.
- 여러 장치와 서버에 대해 `분산 컴퓨팅`을 지원한다.
- Just-in-time 컴파일러를 포함하여 `계산 최적화`를 한다.
- 사용하지 않는 노드 `가지치기` 한다.
- `독립적 연산을 자동으로 병렬처리` 한다.
- `자동미분`, `고성능 옵티마이저`를 제공한다.

## Structure

### 고수준 API

- tf.keras
- tf.estimator

### 저수준 API
- tf.nn
- tf.losses
- tf.metrics
- tf.optimizers
- tf.train
- tf.initializers

### 자동 미분

- tf.GradientTape
- tf.gradients()

### 텐서보드 시각화

- tf.summary()


### 입출력과 전처리

- tf.data
- tf.feature_column
- tf.audio
- tf.image
- tf.io
- tf.queue

### 배포와 최적화

- tf.distribute
- tf.saved_model
- tf.autograph
- tf.graph_util
- tf.lite
- tf.quantization
- tf.tpu
- tf.xla



### 특수한 데이터 구조

- tf.lookup
- tf.nest
- tf.ragged
- tf.sets
- tf.sparse
- tf.strings

### 선형 대수와 신호 처리를 포함한 `수학 연산`

- tf.math
- tf.linalg
- tf.signal
- tf.random
- tf.bitwise

### ETC
- tf.compat
- tf.config
...

