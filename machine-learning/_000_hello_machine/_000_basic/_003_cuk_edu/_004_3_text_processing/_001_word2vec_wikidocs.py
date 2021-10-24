import nltk

from urllib import request
import zipfile
from lxml import etree
import re
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')

# 훈련 데이터 이해하기
request.urlretrieve(
    "https://raw.githubusercontent.com/GaoleMeng/RNN-and-FFNN-textClassification/master/ted_en-20160408.xml",
    filename="ted_en-20160408.xml")

# 영어 문장으로만 구성된 내용을 담고 있는 element => <content></content>
# 파일 열기
targetXML = open('ted_en-20160408.xml', 'r', encoding='UTF-8')
target_text = etree.parse(targetXML)

# xml 파일의 content 내용 가져오기.
parse_text = '\n'.join(target_text.xpath('//content/text()'))
content_text = re.sub(r'\([^)]*\)', '', parse_text)

# 입력 코퍼스에 대해 NLTK를 이용하여 문장 토큰화를 수행
sent_text = sent_tokenize(content_text)

# 각 문장에 대해 구두점을 제거하고, 대문자를 소문자로 변환.
normalized_text = []
for txt in sent_text:
    tokens = re.sub(r'[^a-z0-9]+', ' ', txt.lower())  #
    normalized_text.append(tokens)

result = [word_tokenize(sentence) for sentence in normalized_text]

print(f'총 샘플의 개수 : {len(result)}')

for line in result[3:6]:
    print(line)

# 토큰화된 결과를 word2vec 모델에 훈련시키기.

from gensim.models import Word2Vec

model = Word2Vec(sentences=result,  # 훈련시킬 문장
                 vector_size=100,  # 워드 벡터의 특징 값(임베딩 된 벡터의 차원)
                 window=5,  # 컨텍스트 윈도우 크기
                 min_count=5,  # 최소 빈도 수 (5개보다 적은 단어는 학습하지 않음)
                 workers=4,  # 학습을 위한 프로세스 수, (병렬)
                 sg=0)  # 0은 CBOW, 1은 Skip-gram

# 단어 간 유사성 확인하기
similar_man = model.wv.most_similar('man')
print(similar_man)

# Word2Vec 모델 저장하고 로드하기
from gensim.models import KeyedVectors

model.wv.save_word2vec_format('eng_w2v')  # 모델 저장
loaded_model = KeyedVectors.load_word2vec_format('eng_w2v')  # 모델 불러오기

similar_woman = loaded_model.most_similar('woman')
print(similar_woman)

from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

mpl.rcParams['axes.unicode_minus'] = False
plt.rc('font', family='NanumGothic')


def show_tsne(x, vocab):
    tsne = TSNE(n_components=2)
    X = tsne.fit_transform(x)

    df = pd.DataFrame(X, index=vocab, columns=['x', 'y'])
    # print(df.head())
    fig = plt.figure(figsize=(30, 20))
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(df['x'], df['y'], marker='o')

    for word, pos in df.iterrows():
        ax.annotate(word, pos, fontsize=10)

    plt.xlabel('t-SNE 특성 0')
    plt.ylabel('t-SNE 특성 1')
    plt.show()


def show_pca(x, vocab):
    pca = PCA(n_components=2)
    pca.fit(x)

    # 처음 두 개의 주성분으로 숫자 데이터를 변환
    x_pca = pca.transform(x)

    plt.figure(figsize=(30, 20))
    plt.xlim(x_pca[:, 0].min(), x_pca[:, 0].max())
    plt.ylim(x_pca[:, 1].min(), x_pca[:, 1].max())

    for i in range(len(x)):
        plt.text(x_pca[i, 0], x_pca[i, 1], str(vocab[i]),
                 fontdict={'weight': 'bold', 'size': 9})

    plt.xlabel('첫 번째 주성분')
    plt.ylabel('두 번째 주성분')
    plt.show()


vocabs = list(loaded_model.index_to_key)
X = loaded_model[vocabs]
word_vocab_list = [model.wv[v] for v in vocabs]

sz = 900
show_X = X[:sz, ]
show_vocab = vocabs[:sz]

show_tsne(show_X, show_vocab)
show_pca(show_X, show_vocab)


# HTML 만들기
def show_html(x, vocabs):
    import plotly
    import plotly.graph_objects as go
    pca = PCA(n_components=2)
    pca.fit(x)

    # 처음 두 개의 주성분으로 숫자 데이터를 변환
    x_pca = pca.transform(x)

    fig = go.Figure(data=go.Scatter(x=x_pca[:, 0],
                                    y=x_pca[:, 1],
                                    mode='markers+text',
                                    text=[v for i, v in enumerate(vocabs)]))
    fig.update_layout(title='word2vec')
    fig.show()

    plotly.offline.plot(fig, filename='eng_word2vec.html')


show_html(show_X, show_vocab)
