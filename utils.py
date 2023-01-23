import json
import os



"""Функции которые используем для написания API - эндпоинта"""

def get_posts(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_posts_id(pk):
    for post in get_posts('data/posts.json'):
        if post['pk'] == pk:
            return post
