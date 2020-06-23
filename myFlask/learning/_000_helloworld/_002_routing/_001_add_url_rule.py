import random

from flask import Flask

app = Flask(__name__)
app.debug = True


def index():
    return ""


# add_url_rule 메서드는 뷰 함수를 미리 만들어놓고 라우팅 지정을 하려 할 때 사용한다.
app.add_url_rule("/", "index", index)

""" [route] [add_url_rule] argument 정리
    defaults: URL 변수에 기본값을 지정하는 옵션,
        TYPE: Dictionary 타입으로 전달한다.
        
    methods: Http Method 지정 옵션,
        TYPE: 문자열 리스트
        
    host: 라우팅 요청이 어떤 호스트에 응답할지 지정.
    TYPE: 문자열
    
    subdomain: 뷰 함수가 특정 서브 도메인에만 응답하도록 지정하는 옵션,
        TYPE: 문자열
          
    redirect_to: 라우팅 요청을 받았을 경우 다른 곳으로 요청을 전달,
            TYPE: 
                - 문자열 값
                - 리다이렉션 함수를 인자로 받는다.
                    * 변수 값을 처리할 어댑터와 변수 값을 인자로 받는다.
    
    alias: endpoint 옵션과 같은 역할을 한다.
"""


@app.route("/person/<person_id>")
@app.route("/person", defaults={"person_id": random.choice(range(100))})
def board(person_id):
    return "{0}번 사람을 호출하였습니다.".format(person_id)


@app.route("/board", host="example.com")
def board_host():
    return "/board URL을 호출하였습니다."


if __name__ == '__main__':
    app.run()
