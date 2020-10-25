from sklearn.feature_extraction.text import TfidfVectorizer

"""
자주 등장하는 단어의 횟수와
특정 단어가 자주 등장하지 않을수록 값이 커진다는 것을 의미

연산
Tf * Idf
"""

text_data = ['나는 배가 고프다', '내일 점심 뭐먹지', '내일 공부 해야겠다', '점심 먹고 공부 해야지']

# 사전 만들기
tfidf_vectorizer = TfidfVectorizer()
tfidf_vectorizer.fit(text_data)
# 사전 확인하기
print(tfidf_vectorizer.vocabulary_)

# 문장 추출하기
sentence = [text_data[3]]
print(tfidf_vectorizer.transform(sentence).toarray())

sentence2 = [text_data[2]]
print(tfidf_vectorizer.transform(sentence2).toarray())

result = tfidf_vectorizer.transform(sentence).toarray() * tfidf_vectorizer.transform(sentence2).toarray()
print(result)