from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam adipisci error suscipit minus quo assumenda ' \
       'culpa, veniam molestias dolorem voluptatum asperiores amet magni vitae est eaque reprehenderit quis vel fugit! '

sent_text = sent_tokenize(text)

print(sent_text)

vocabulary = {}
sentences = []

stop_words = stopwords.words('english')

for sent in sent_text:
    sentence = word_tokenize(sent)
    res = []

    for word in sentence:
        _word = word.lower()
        if word not in stop_words and len(word) > 2:
            res.append(word)
            if word not in vocabulary:
                vocabulary[word] = 0

            vocabulary[word] += 1

    sentences.append(res)

print(sentences)

