import os

from flask import Flask, render_template,request
from post_manager import PostManager

app = Flask(__name__)
post_manager = PostManager(os.path.join("data","posts.json"))


@app.route('/')
def index():
    posts = post_manager.get_posts_all(os.path.join("data","posts.json"))
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def index_1(post_id):
    post = post_manager.get_post_by_pk((post_id))
    coments = post_manager.get_comments_by_post_id((post_id))
    count_coments = len(coments)
    return render_template('post.html', post=post, coments=coments, count_coments=count_coments)


@app.route('/search', methods=['GET'])
def index_2():
    query = request.args.get('s')
    found = post_manager.search_for_posts('query')
    return render_template('search.html', posts=found)


@app.route('/users/<user_name>')
def index_3(user_name):
    user = post_manager.get_posts_by_user(user_name)
    return render_template('user-feed.html', user=user)








if __name__ == '__main__':
    app.run(debug=True, port = 5010)




