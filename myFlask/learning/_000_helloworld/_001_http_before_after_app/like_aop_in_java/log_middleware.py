import logging
from future.backports.urllib.parse import unquote_plus


class LogMiddleware(object):
    """WSGI middleware for collecting site usage"""

    def __init__(self, app):
        self.app = app

    # 호출 메서드 이름은 반드시 __call__을 사용해야한다.
    # arguments 의 관례는 environ, start_response
    def __call__(self, environ, start_response):
        url = environ.get("PATH_INFO", "")

        query = unquote_plus(environ.get("QUERY_STRING", ""))
        logging.info(msg=query)

        # item = logging.LogRecord(
        #     name="Logging",
        #     level=logging.INFO,
        #     pathname=url,
        #     lineno=0,
        #     msg=query,
        #     args=None,
        #     exc_info=None
        # )

        # logging.handle(item)

        return self.app(environ, start_response)