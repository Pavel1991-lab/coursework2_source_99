from main import get_all_posts, get_one_posts, app
from post_manager import PostManager
import json
import os

post_manager = PostManager(os.path.join("data","posts.json"))
posts = post_manager


def test_get_all_posts():
    test_post = []
    with open('data/posts.json', 'r', encoding='utf-8') as file:
        test_post = json.load(file)
    print(test_post)
    print(posts.get_posts_all('data/posts.json'))
    print(test_post == posts.get_posts_all('data/posts.json'))


keys_should_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}


def test_api_all_posts():
    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == keys_should_be
    print(response.status_code)
    print(type(api_response))
    print(api_response[0].keys())


def test_api_post():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response.keys()) == keys_should_be