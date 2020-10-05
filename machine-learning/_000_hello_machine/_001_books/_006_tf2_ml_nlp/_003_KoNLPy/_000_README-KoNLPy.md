# KoNLPy

    java 1.7 이상
    별도의 형태소 분석기를 설치
    한글 자연어처리를 위한 오픈소스 라이브러리
    
    일반적인 어절 단위에 대한 토크나이징은 NLTK로 해결 가능
    
    형태소 단위에 대한 토크나이징을 위한 학습
 
windows 설치 
-    
> pip install JPype1-0.63-cp36-cp36m-win_amd64.whl
>
> pip install konlpy

---
ubuntu 설치
- 

> pip3 install konlpy
>

KoNLPy 내 다양한 형태소 분석기들
-

- Hannanum
- Kkma
- Komoran
- Mecab
- Okt(Twitter) 



Okt
=

okt.morphs()
-

    텍스트를 형태소 단위로 나눈다.

> norm: Bool
>
>   > 문장을 정규화하는 역할
>   >
>   > default: false
>
> stem: Bool
>   > 각 단어에서 어간을 추출하는 기능
>   >
>   > default: false
>

okt.nouns()
-

    텍스트에서 `명사`만 뽑아낸다.
    

okt.phrases()
-

    텍스트에서 `어절`을 뽑아낸다.
    
okt.pos()
-

    각 품사를 태깅하는 역할
    
    태깅이란:
    주어진 텍스트를 형태소 단위로 나누고,
    나눠진 각 형태소를 그에 해당하는 품사와 함께 리스트화하는 것을 의미

> join: Bool
>   
>   > 형태소와 품사를 `형태소/품사` 형태로 붙여서
>   > 리스트화한다.
>
> norm: Bool
>   
>   > 문장 정규화
>
> stem: Bool
>   
>   > 각 단어의 어간을 추출
>   
>   > ex: `해야지` => `하다`