from main.base.api_client import APIClient


class PostService:
    def __init__(self, client: APIClient):
        self.client = client

    def get_posts(self):
        return self.client.get_posts()

    def get_posts_by_user(self, user_id):
        """Return all posts by a specific user."""
        posts = self.get_posts()
        return [post for post in posts if post['userId'] == user_id]

    def user_has_more_than_n_posts(self, user_id, n):
        """Return True if the user has more than n posts."""
        posts = self.get_posts_by_user(user_id)
        return len(posts) > n
