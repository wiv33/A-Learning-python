from flask import Flask, request

app = Flask(__name__)


@app.route("/example/environ", methods=["GET", "POST"])
def example_environ():
    ret_str = ("REQUEST_METHOD: %(REQUEST_METHOD)s<br/>"
               "SCRIPT_NAME: %(SCRIPT_NAME)s<br/>"
               "PATH_INFO: %(PATH_INFO)s<br/>"
               "QUERY_STRING: %(QUERY_STRING)s<br/>"
               # "CONTENT_TYPE: %(CONTENT_TYPE)s<br/>"
               "SERVER_NAME: %(SERVER_NAME)s<br/>"
               "SERVER_PORT: %(SERVER_PORT)s<br/>"
               "SERVER_PROTOCOL: %(SERVER_PROTOCOL)s<br/>"
               "wsgi.version: %(wsgi.version)s<br/>"
               "wsgi.url_scheme: %(wsgi.url_scheme)s<br/>"
               "wsgi.input: %(wsgi.input)s<br/>"
               "wsgi.errors: %(wsgi.errors)s<br/>"
               "wsgi.multithread: %(wsgi.multithread)s<br/>"
               "wsgi.multiprocess: %(wsgi.multiprocess)s<br/>"
               "wsgi.run_once: %(wsgi.run_once)s"
               ) % request.environ

    return ret_str


if __name__ == '__main__':
    app.run("example.com",
            port=5000,
            debug=True)