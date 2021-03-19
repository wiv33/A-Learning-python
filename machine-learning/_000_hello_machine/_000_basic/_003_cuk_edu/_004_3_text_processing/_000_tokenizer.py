from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam adipisci error suscipit minus quo assumenda ' \
       'culpa, veniam molestias dolorem voluptatum asperiores amet magni vitae est eaque reprehenderit quis vel fugit! '

result = sent_tokenize(text)

print(result)

vocabulary = {}
sentences = []

stop_words = stopwords.words('english')

for sent in sentences:
       sentence = word_tokenize(sent)
       res = []

       for word in sentence:
              pass


