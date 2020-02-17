from flask import Flask, request

app = Flask(__name__)

# Query를 ?question=answer 로 호출하였다.
@app.route("/board")
def board_list():
    return "쿼리 스트링 question 변수의 값은 {}입니다."\
        .format(request.args.get("question"))

# Get 방식의 Query String
# /board2?article=10
@app.route("/board2")
def board():
    """
    request.args.get(:param_key, [:default_value], [:type])
    :return:
    """
    article_id = request.args.get("article", "2", int)
    return str(article_id)


if __name__ == '__main__':
    app.run(host="example.com",
            port=5000,
            debug=True)