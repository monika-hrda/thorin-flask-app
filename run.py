import os
import json
from flask import Flask, render_template, request


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
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form["email"])
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":  # 'main' = name of the default module in Python
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
