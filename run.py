import os
from flask import Flask


# Instance of Flask class;
# 1st arg = name of the application's module - our package;
# we're just using a single module, __name__ is a built-in Python variable
# Flask needs this to know where to look for templates and static files
app = Flask(__name__)


@app.route("/")   # decorator; @ = pie-notation
def index():
    return "Hello, World"


if __name__ == "__main__":  # 'main' = name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
