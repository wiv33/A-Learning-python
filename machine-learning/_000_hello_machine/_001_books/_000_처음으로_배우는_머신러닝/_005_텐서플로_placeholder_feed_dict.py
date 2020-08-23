import tensorflow as tf

"""
placeholder, feed_dict

텐서플로 연산 그래프에 입력 데이터를 넣기 위해 사용된다.

placeholder:
    변수 -> 구체적인 형태나 값이 정해지지 않은 임시 변수
feed_dict:
    플레이스홀더(placeholder)와 실제값을 연결하는 역할을 한다.
    placeholder 안에 값을 채워 넣는다.

"""
with tf.Session() as session:
    input1 = tf.placeholder(tf.float32, (3, 2))  # :type, :shape
    input2 = tf.placeholder(tf.float32)

    output = tf.multiply(input1, input2)  # 두 입력을 곱셈한다.

    print(session.run([output], feed_dict={input1: [[1., 2.], [4., 5.], [6., 7.]], input2: [3., 2]}))
