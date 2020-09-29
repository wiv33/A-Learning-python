from sklearn.feature_extraction.text import CountVectorizer

"""
텍스트 데이터에서 횟수 기준으로 추출하는 방법
단위의 정의는 선택
"""

# 각 단어의 길이를 맞추어야 하는지?
#  No
text_data = ['나는 배가 고프다', '내일 점심 뭐먹지', '내일 공부 해야겠다', '점심 먹고 공부 해야지']

count_vectorized = CountVectorizer()
count_vectorized.fit(text_data)
print(count_vectorized.vocabulary_)

sentence = [text_data[0]]
print(count_vectorized.transform(sentence).toarray())

