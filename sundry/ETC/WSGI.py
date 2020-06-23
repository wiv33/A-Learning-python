from wsgiref.simple_server import make_server


def application(environ, start_response):
    response_body = ['%s:%s' % (key, value)
                     for key, value in sorted(environ.items())]
    response_body = '\n'.join(response_body)

    status = '200 OK'
    response_headers = [('Content-type', 'text/plan'), ('Content-Length', str(len(response_body)))]

    start_response(status, response_headers)

    return [response_body.encode("utf8")]


httpd = make_server(
    'localhost',
    8051,
    application
)

httpd.handle_request()
