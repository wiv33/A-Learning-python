import collections
import logging

import flask
from flask import Flask, request

""" request 객체에서 param 꺼내기 예제
    1. Query String
      1-1 default 값 정하기
      1-2 type 정하기
      
    2. form submit 시 param 꺼내기
      2-1 header 설정 주석
    
    3. values 속성의 param
      3-1 CombinedMultiDict :type
        - MultiDict 데이터 타입들이 합쳐진 형태 
"""

app = Flask(__name__)


# 1. Query를 ?question=answer 로 호출하였다.
@app.route("/board")
def board_list():
    return "쿼리 스트링 question 변수의 값은 {}입니다." \
        .format(request.args.get("question"))


# 2. Get 방식의 Query String
# /board2?article=10
@app.route("/board2")
def board():
    """
    request.args.get(:param_key, [:default_value], [:type])
    :return:
    """
    article_id = request.args.get("article", "2", int)
    return str(article_id)


# 3. form submit
# request.*form*.get 이 되었다.
# Content-Type : application/x-www-form-urlencoded
@app.route("/boardForm", methods=["POST"])
def board_form():
    article_id = request.form.get("article", "3", int)
    return str(article_id)


# 4. GET과 POST 를 동시에 선언했을 경우
# GET의 values 값을 가져옴 / GET이 이긴다고 보면 된다.
@app.route("/boardGetPost", methods=["GET", "POST"])
def board_get_post():
    return request.values.get("question")


import json

cnt_dict: {str: int} = {}

import logging


@app.route("/sample", methods=["POST"])
def sample_payload():
    logging.info("req : {}", request.headers.get("Header"))
    import asyncio
    asyncio.run(update_dict(request))
    return "success"


async def update_dict(request):
    file_name = request.headers.get("Header")
    data = json.loads(request.data)
    logging.info(file_name, len(str(data)))
    if file_name in cnt_dict:
        get_item = cnt_dict.get(file_name, file_name)
        cnt_dict.update({file_name: int(get_item) + 1})
    else:
        cnt_dict.setdefault(file_name, 1)


@app.route("/sample-rest", methods=["POST"])
def sample_payload_xml():
    import xml.etree.ElementTree as et
    data = request.data

    xml = et.fromstring(data)
    print(xml.attrib)

    file_name = xml.attrib['filename']
    print(file_name)
    if file_name in cnt_dict:
        get_item = cnt_dict.get(file_name, file_name)
        cnt_dict.update({file_name: int(get_item) + 1})
    else:
        cnt_dict.setdefault(file_name, 1)

    return cnt_dict


@app.route("/cnt", methods=["GET"])
def get_cnt():
    return {"a_total": len(cnt_dict.values()), "body": cnt_dict}


if __name__ == '__main__':
    from werkzeug.serving import WSGIRequestHandler
    WSGIRequestHandler.protocol_version = "HTTP/1.1"
    app.run(host="localhost",
            port=5000,
            debug=True)
