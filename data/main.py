from flask import Flask, request, render_template
from data import utils
from data.utils import PostManager
from data import utils
import json
app = Flask(__name__)
post_manager = PostManager("posts.json")


@app.route('/')
def index():
    posts = post_manager.get_posts_all(("posts.json"))
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True, port = 5010)
