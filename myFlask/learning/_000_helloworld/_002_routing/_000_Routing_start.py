from flask import Flask, make_response, url_for

app = Flask(__name__)

app.debug = True

myDictionary = {"my_name":"pil_seong", "skill":"hot"}

@app.route("/")
def hello_world():
    return "Hello World BODY!!"

@app.route("/board", methods=['GET'])
def board_list():
    print("board_list")
    return make_response(('flask framework', 200, {"program": "language python"}))

@app.route("/board", methods=['POST'])
def post_board_list():
    return make_response("POST BODY")

# PathVariable <name>
@app.route('/board/<name>')
def end_point_board_list(name):
    return make_response("end_point=boarder, get Name {0}".format(name))

with app.test_request_context('/'):
    print("run ! test_request_context")
    print(url_for('board_list'))
    print(url_for('post_board_list'))

if __name__ == '__main__':
    app.run()