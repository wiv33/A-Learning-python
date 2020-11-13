from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)


class HelloForm(Form):
    say_hello = TextAreaField('', [validators.DataRequired()])


@app.route("/")
def index():
    # Flask 내 request
    form = HelloForm(request.form)
    return render_template('index.html', form=form)


@app.route("/hello", methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == "POST" and form.validate():
        name = request.form['say_hello']
        return render_template('hello.html', name=name)
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run()
