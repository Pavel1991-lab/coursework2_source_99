import json
import os


class PostManager:
    def __init__(self,path):
        self.path = path

    def get_posts_all(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_posts_by_user(self,user_name):
        for post in self.get_posts_all('data/posts.json'):
            if post['poster_name'] == user_name:
                return post
            if post['poster_name'] == user_name and len(post["content"]) == 0:
                return []
        return f'Vallue Error'

    def get_comments_by_post_id(self,post_id):
        b = []
        for coment in self.get_posts_all('data/comments.json'):
            if coment['post_id'] == post_id:
                b.append(coment)
        return b

    def search_for_posts(self,querry):
        a = []
        for i in self.get_posts_all('data/posts.json'):
            if querry.lower() in i["content"].lower():
                a.append(i)
        return a

    def get_post_by_pk(self,pk):
        for post in self.get_posts_all('data/posts.json'):
            if post['pk'] == pk:
                return post


