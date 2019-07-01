from flask import Flask
app = flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

if __name__ == '__main__':
    app.run(port=4000, debug=True)

