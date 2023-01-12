from flask import Flask, request, render_template
from data import utils
from data.utils import PostManager
app = Flask(__name__)


@app.route('/')
def index():
    posts = PostManager.get_posts_all("posts.json")
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True, port = 5010)

