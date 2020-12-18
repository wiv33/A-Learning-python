from nltk.stem import SnowballStemmer, WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

sentence = '\nPower ballad\n\n\n\n\n\n\n\nSinger Ji Se-hee performs her new song “Not Yet…” ' \
           'on Tuesday at the Ilchi Art Hall, southern Seoul. “Not Yet…” is a powerful ballad' \
           ' about how one must get back up after a tearful breakup. Ji made her debut in 2008. [NEWS1]'

stemmer = SnowballStemmer('english')
stop = set(stopwords.words('english'))

words = word_tokenize(sentence)

result = [stemmer.stem(word) for word in words]
print(' '.join(result))
print("-" * 100)
#
lem = WordNetLemmatizer()
res = [lem.lemmatize(word) for word in words]

print(' '.join(res))

print("*" * 100)

p = PorterStemmer()
res3 = [p.stem(word) for word in words]
print(' '.join(res3))
