from flask import Flask, request, redirect, make_response

app = Flask(__name__)

@app.route("/example/cookie")
def example_cookie():
    print(request.cookies)
    return ""


@app.route("/example/cookie_set")
def example_cookie_set():
    redirect_to_cookie = redirect("/example/cookie")
    response = make_response(redirect_to_cookie)
    response.set_cookie("Cookie Register", value='Example Cookie')
    return response


if __name__ == '__main__':
    app.run("example.com"
            ,port=5000,
            debug=True)
