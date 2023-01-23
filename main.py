import datetime
import os

from flask import Flask, render_template,request, jsonify
from post_manager import PostManager
from utils import get_posts, get_posts_id
import logging
logging.basicConfig(filename='log/basic.log', level=logging.INFO, encoding='utf-8')

app = Flask(__name__)
post_manager = PostManager(os.path.join("data","posts.json"))
app.config['JSON_AS_ASCII'] = False

"""
Вьюшка которая получает все посты
"""

@app.route('/')
def index():
    posts = post_manager.get_posts_all(os.path.join("data","posts.json"))
    return render_template('index.html', posts=posts)

"""
Вьюшка которая получает пост по айди
"""
@app.route('/post/<int:post_id>')
def index_1(post_id):
    post = post_manager.get_post_by_pk((post_id))
    coments = post_manager.get_comments_by_post_id((post_id))
    count_coments = len(coments)
    return render_template('post.html', post=post, coments=coments, count_coments=count_coments)




"""
Вьюшка с помощью которой ищем посты
"""
@app.route('/search', methods=['GET'])
def index_2():
    query = request.args.get('s')
    found = post_manager.search_for_posts(query)
    return render_template('search.html', posts=found)



"""
Вьюшка которая покажет пост по имени
"""
@app.route('/users/<user_name>')
def index_3(user_name):
    user = post_manager.get_posts_by_user(user_name)
    return render_template('user-feed.html', user=user)


@app.errorhandler(404)
def page_not_found(e):
    """
    Обработчик запросов к несуществующим страницам.
    :param e: выводит 'Ошибка 404, Страница отсутствует'.
    :return: возвращает статус-код 404.
    """
    # устанавливаем статус 404 явно
    return 'Ошибка 404, Страница отсутствует', 404


@app.errorhandler(500)
def page_not_found(e):
    """
    Обработчик ошибок, возникших на стороне сервера.
    :param e: выводит 'Ошибка 500, Внутренняя ошибка сервера'.
    :return: возвращает статус код 500.
    """
    # устанавливаем статус 500 явно
    return 'Ошибка 500, Внутренняя ошибка сервера', 500


"""
Представление, которое обрабатывает запрос GET /api/posts
"""

@app.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info('Запрос /api/posts/')
    a = get_posts('data/posts.json')
    return jsonify(a)

"""
Представление, которое обрабатывает запрос GET /api/posts/<post_id>
"""


@app.route('/api/posts/<int:postid>', methods=['GET'])
def get_one_posts(postid):
    logging.info(f'{datetime.datetime.now()} [INFO] Запрос /api/posts/{postid} ')
    a = get_posts_id(postid)
    return jsonify(a)




if __name__ == '__main__':
    app.run(debug=True, port = 5010)




