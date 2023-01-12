import json

class PostManager:
    def __init__(self,path):
        self.path = path

    def get_posts_all(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

    def get_posts_by_user(self,user_name):
        for post in self.get_posts_all('posts.json'):
            if post['poster_name'] == user_name:
                return post["content"]
            if post['poster_name'] == user_name and len(post["content"]) == 0:
                return []
        return f'Vallue Error'

    def get_comments_by_post_id(self,post_id):
        b = []
        d = []
        for coment in self.get_posts_all('comments.json'):
            if coment['post_id'] == post_id:
                b.append(coment["comment"])
            d.append(coment["post_id"])
        if post_id not in d:
            return f'Vallue Error'
        return b

    def search_for_posts(self,querry):
        a = []
        for i in self.get_posts_all('posts.json'):
            if querry.lower() in i["content"].lower():
                a.append(i["content"])
        return a

    def get_post_by_pk(self,pk):
        for post in self.get_posts_all('posts.json'):
            if post['pk'] == pk:
                a = post["content"]
        return a

post_manager = PostManager("posts.json")
print(post_manager.search_for_posts('ага'))

