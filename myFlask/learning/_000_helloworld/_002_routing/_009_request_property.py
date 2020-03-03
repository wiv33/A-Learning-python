from flask import Flask, request

app = Flask(__name__)


@app.route("/example/environ", methods=["GET", "POST"])
def example_environ():
    return ("path: %s<br/>"
            "script_root: %s<br/>"
            "url: %s<br/>"
            "base_url: %s<br/>"
            "url_root: %s<br/>") % (request.path, request.script_root,
                                    request.url, request.base_url,
                                    request.url_root)


if __name__ == '__main__':
    app.run("example.com",
            5000,
            True)
