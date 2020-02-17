from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

def date_korean_type(date_format):
    def translate(date_str):
        return datetime.strptime(date_str, date_format)
    return translate

@app.route("/board", methods=["GET", "POST"])
def date_time_board():
    my_date = request.values.get("date", "2020-02-17", type=date_korean_type("%Y-%m-%d"))
    print(my_date)
    return "날짜는 콘솔을 확인하세요. {}".format(my_date)

if __name__ == '__main__':
    app.run("example.com",
            port=5000,
            debug=True)