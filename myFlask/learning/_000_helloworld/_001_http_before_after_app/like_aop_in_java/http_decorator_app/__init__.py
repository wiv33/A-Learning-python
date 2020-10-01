from flask import Flask

from myFlask.learning._000_helloworld._001_http_before_after_app.like_aop_in_java.log_middleware import LogMiddleware

""" 요청 전후 핸들러
    
    - before_first_request: 웹 앱 기동 후 가장 처음에 들어오는 http 요청에서만 실행
    - before_request: 매 HTTP 요청이 올 때마다 실행
    - after_request: 매 HTTP 요청이 끝나 브라우저에 응답하기 전에 실행
    - teardown_request: HTTP 요청의 결과가 브라우저에 응답한 다음 실행
    - teardown_appcontext: HTTP 요청이 완전히 완료되면 실행되며, 애플리케이션 컨텍스트 내에서 실행된다. 
     
"""

app = Flask(__name__)

# 미들웨어 등록
app.wsgi_app = LogMiddleware(app.wsgi_app)

# Debug mode
# 두 설정의 결과는 같다.
# ajax, rest API 호출 시에는 사용할 수 없다는데......
app.debug = True
app.config.update(DEBUG=True)


@app.route("/")
def http_prepost_response():
    return "데헷"


@app.before_first_request
def before_first_request_test():
    print("앱 기동되고 첫 HTTP 요청에 실행")


@app.before_request
def before_request_test():
    print("매 HTTP 요청이 응답하기 전에 실행")


@app.after_request
def after_request_test(response):
    print("매 HTTP 요청 후 실행")
    return response


@app.teardown_request
def teardown_request_test(exception):
    print("매 HTTP 요청의 결과가 브라우저에 응답된 후 호출")


@app.teardown_appcontext
def teardown_appcontext_test(exception):
    print("HTTP 요청의 애플리케이션 컨텍스트가 종료될 때 실행")
