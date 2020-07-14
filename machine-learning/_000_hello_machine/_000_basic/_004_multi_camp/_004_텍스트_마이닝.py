import codecs
import rx
from rx import operators as ops
from konlpy.tag import Komoran, Twitter


def print_word(word, filter_word):
    extract_word(word, filter_word).subscribe(lambda x: print("{}".format(x)))


def extract_word(word, filter_word):
    return rx.from_(word).pipe(
        ops.filter(lambda tup: tup[1] == filter_word and len(tup[0]) > 1),
        ops.map(lambda tup: tup[0]),
        ops.reduce(lambda acc, t1: acc + " " + t1)
    )


file = open("article.txt", mode='r', encoding='utf-8')

article = file.read()

model = Komoran()
komoran_pos = model.pos(article)

print_word(komoran_pos, "NNP")

twitter = Twitter()
twitter_pos = twitter.pos(article)

# print(twitter_pos)

print_word(twitter_pos, "Noun")

from sklearn.feature_extraction.text import TfidfVectorizer

