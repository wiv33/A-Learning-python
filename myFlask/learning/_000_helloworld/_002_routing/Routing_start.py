from flask import Flask, make_response

app = Flask(__name__)

app.debug = True

myDictionary = {"my_name":"pil_seong", "skill":"hot"}

@app.route("/")
def hello_world():
    return "Hello World BODY!!"

@app.route("/board", methods=['GET'])
def board_list():
    return make_response(('flask framework', 200, {"program": "language python"}))


@app.route("/board", methods=['POST'])
def post_board_list():
    return make_response("POST BODY")

if __name__ == '__main__':
    app.run()