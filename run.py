import os
from flask import Flask, render_template


# Instance of Flask class;
# 1st arg = name of the application's module - our package;
# we're just using a single module, __name__ is a built-in Python variable
# Flask needs this to know where to look for templates and static files
app = Flask(__name__)


@app.route("/")   # decorator; @ = pie-notation
def index():     # this function is also called a view
    return render_template("index.html")


# bind the path of the decorator to a view called about()
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":  # 'main' = name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
