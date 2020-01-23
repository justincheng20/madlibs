from flask import Flask, render_template, request
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "oh-so-secret"
# debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    title = "Mad Libs"
    return render_template("index.html",words=story.prompts,title=title)

@app.route("/story")
def make_story():
    ans = dict(request.args)
    return (f'<h1>Story</h1> <p>{story.generate(ans)}</p>')
