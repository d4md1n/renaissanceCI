from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/test')
def test_world():
    return """<html>
              <head><title>Sample Html</title></head>
              <body>
                <h3> Sample Html</h3>
              </body>
              </html>"""


if __name__ == '__main__':
    app.run()
