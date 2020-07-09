import codecs
import rx
from rx import operators as ops
from konlpy.tag import Komoran, Twitter


def print_word(word, filter_word):
    rx.from_(word).pipe(
        ops.filter(lambda tup: tup[1] == filter_word and len(tup[0]) > 1),
        ops.map(lambda tup: tup[0])
    ).subscribe(lambda x: print("word is {}".format(x)))


file = open(
    "C:\\Users\\user\\PycharmProjects\\"
    "learning-python\\machine-learning\\_000_hello_machine\\_000_basic\\_004_multi_camp\\article.txt", mode='r',
    encoding='utf-8')

article = file.read()

model = Komoran()
komoran_pos = model.pos(article)

print_word(komoran_pos, "NNP")

twitter = Twitter()
twitter_pos = twitter.pos(article)

print(twitter_pos)

print_word(twitter_pos, "Noun")
