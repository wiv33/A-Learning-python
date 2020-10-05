import nltk
from tokenize import tokenize
from konlpy.tag import Okt

pos_tagger = Okt()


def read_data(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[:1]

    return data


train_data = read_data('./data/나이브_베이즈_분류/ratings_train.txt')
test_data = read_data('./data/나이브_베이즈_분류/ratings_test.txt')

train_docs = [(tokenize(row[1]), row[2]) for row in train_data[:5000]]
test_docs = [(tokenize(row[1]), row[2]) for row in test_data[:5000]]

tokens = [t for d in train_docs for t in d[0]]
text = nltk.Text(tokens=tokens, name='NMSC')

selected_words = [f[0] for f in text.vocab().most_common(2000)]


def term_exists(doc):
    return {'exists[{}]'.format(word): (word in set(doc)) for word in selected_words}


train_xy = [(term_exists(d), c) for d, c in train_docs]
test_xy = [(term_exists(d), c) for d, c in test_docs]

classifier = nltk.NaiveBayesClassifier.train(train_xy)
print(nltk.classify.accuracy(classifier=classifier, gold=test_xy))