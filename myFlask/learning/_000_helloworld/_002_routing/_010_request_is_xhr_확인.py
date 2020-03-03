from flask import Flask, request

app = Flask(__name__)

@app.route("/example/environ", methods=['GET', 'POST'])
def example_environ_is_xhr():
    print(request.is_xhr)
    return ""

if __name__ == '__main__':
    app.run("example.com",
            5000,
            True)
