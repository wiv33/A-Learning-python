from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

import numpy as np
from collections import Counter

text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam adipisci error suscipit minus quo assumenda ' \
       'culpa, veniam molestias dolorem voluptatum asperiores amet magni vitae est eaque reprehenderit quis vel fugit! '

sent_text = sent_tokenize(text)

print(sent_text)

vocabulary = {}
sentences = []

stop_words = stopwords.words('english')

for sent in sent_text:
    sentence = word_tokenize(sent)
    result = []

    for word in sentence:
        _word = word.lower()
        if word not in stop_words and len(word) > 2:
            result.append(word)
            if word not in vocabulary:
                vocabulary[word] = 0

            vocabulary[word] += 1

    sentences.append(result)

print(sentences)

print(vocabulary)

# 두 번 이상 등장한 단어들의 빈도수 기준으로 단어에 정수값 부여하기
sorted_vocabulary = sorted(vocabulary.items(), key=lambda x: x[1], reverse=True)
print(sorted_vocabulary)

integer_embedding = {}
i = 0
for (word, frequency) in sorted_vocabulary:
    if frequency > 1:
        i = i + 1
        integer_embedding[word] = i

print(integer_embedding)

# 빈도수 기준 정수 인코딩 - Counter
words = np.hstack(sentences)
print(words)

vocabulary_counter = Counter(words)
print(vocabulary_counter)

vocab_size = 4
common_vocabulary = vocabulary.most_common(vocab_size)
print(common_vocabulary)

# Counter 활용
integer_embedding = {}
i = 0
for (word, frequency) in common_vocabulary:
    i = i + 1
    integer_embedding[word] = i

print(integer_embedding)

# Counter 활용 끝

import numpy as np
from collections import Counter

print(sentences)
