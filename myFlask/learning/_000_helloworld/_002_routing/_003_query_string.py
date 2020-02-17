from flask import Flask, request

app = Flask(__name__)

# Query를 ?question=answer 로 호출하였다.
@app.route("/board")
def board_list():
    return "쿼리 스트링 question 변수의 값은 {}입니다.".format(request.args.get("question"))


if __name__ == '__main__':
    app.run(host="example.com",
            port=5000,
            debug=True)