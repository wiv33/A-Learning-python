from flask import Flask

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
