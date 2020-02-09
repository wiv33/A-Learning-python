import sqlite3

from flask import Flask
from flask import g


"""Flask 인자로 전달할 수 있는 Parameter
    * required
    - choice
    
    * import_name: 애플리케이션 패키지의 이름을 지정하는 인자로 문자열 값을 정의한다.
                    보통 __name__ 변수를 넘겨 이름을 생성한다.
    
    - static_url_path: 정적 파일을 서비스 하는 [static_folder]를 웹에서 접근할 때 
                        어떤 경로로 사용할 것인지 지정한다.
                        '/' 문자로 시작할 수 없고, 기본 값은 static
    
    - static_folder: 프로그램 소스 트리에서 정적 파일을 서비스하는 폴더명을 지정한다.
                        기본 값은 static
    
    - template_folder: 프로그램 소스 트리에서 뷰 함수가 사용할 HTML 파일이 위치하는 폴더명을 지정한다.
                        기본 값은 templates
                        
    Flask __init__ 함수의 인자 목록
        import_name,
        static_url_path=None,
        static_folder="static",
        static_host=None,
        host_matching=False,
        subdomain_matching=False,
        template_folder="templates",
        instance_path=None,
        instance_relative_config=False,
        root_path=None,                         

"""

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


"""  Flask 의 Global 객체 사용의 예.
#
    @app.before_request 데코레이터는 http 요청이 올 때마다 실행되고
    
    @app.teardown_request 데코레이터는 http 요청에 대한 응답이 이루어질 때 호출된다.
#

#
    g.db에 config에 저장된 DATABASE 설정을 저장한다.
    
    getattr 함수로 Flask 글로벌 객체에서 db 속성을 가져오고 없을 경우 None을 db에 대입한다.
    None이 아닐 경우 Connection 을 닫는다.
#    

#
    Flask 가 지원하는 5가지 사용자 응답 객체
    
    - response_class: Response 클래스로부터 생성한 인스턴스 객체
    - str: 유니코드가 아닌 일반 문자열
    - unicode: 유니코드 문자열 (Python 2 버전에만 있음)
    - WSGI 함수: 프로그래머가 정의한 WSGI 함수는 호출되면 버퍼링된 응답 객체로 반환된다.
    - tuple: (response, status, headers) 형식의 튜플을 인자로 제공 받는다.
            response 는 response_class, str, unicode, WSGI 중 하나만 올 수 있다.
            status 는 Java HttpStatus 객체를... 파이썬 Dictionary 형식으로 제공
"""
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()