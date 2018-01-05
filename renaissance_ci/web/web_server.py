from flask import Flask, render_template
import renaissance_ci.core.chain
from test import *

app = Flask(__name__)

app.template_folder = '../resources/templates'
print(renaissance_ci.core.chain.PipelineChainLink.__subclasses__())


# @app.route('/test')
# def test_world():
#     return """<html>
#               <head><title>Sample Html</title></head>
#               <body>
#                 <h3> Sample Html</h3>
#               </body>
#               </html>"""


@app.route('/')
def test_template():
    return render_template("home.html",
                           name="billy",
                           result=renaissance_ci.core.chain.PipelineChainLink.__subclasses__())


if __name__ == '__main__':
    app.run()
