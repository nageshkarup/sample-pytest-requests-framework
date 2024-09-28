import requests
from utils.constants import BASE_URL


class APIClient:
    @staticmethod
    def _make_request(method, endpoint, **kwargs):
        url = f"{BASE_URL}/{endpoint}"
        response = requests.request(method, url, timeout=60, **kwargs)
        response.raise_for_status()
        return response.json()

    def get(self, endpoint):
        """Handles GET requests."""
        return self._make_request("GET", endpoint)

    def post(self, endpoint, data):
        """Handles POST requests."""
        return self._make_request("POST", endpoint, json=data)

    def put(self, endpoint, data):
        """Handles PUT requests."""
        return self._make_request("PUT", endpoint, json=data)

    def delete(self, endpoint):
        """Handles DELETE requests."""
        return self._make_request("DELETE", endpoint)

    # Users
    def get_users(self):
        return self.get('users')

    def get_user_by_id(self, user_id):
        return self.get(f'users/{user_id}')

    def create_user(self, user_data):
        return self.post('users', user_data)

    def update_user(self, user_id, user_data):
        return self.put(f'users/{user_id}', user_data)

    def delete_user(self, user_id):
        return self.delete(f'users/{user_id}')

    # Todos
    def get_todos(self):
        return self.get('todos')

    def get_todo_by_id(self, todo_id):
        return self.get(f'todos/{todo_id}')

    def create_todo(self, todo_data):
        return self.post('todos', todo_data)

    def update_todo(self, todo_id, todo_data):
        return self.put(f'todos/{todo_id}', todo_data)

    def delete_todo(self, todo_id):
        return self.delete(f'todos/{todo_id}')

    # Posts
    def get_posts(self):
        return self.get('posts')

    def get_post_by_id(self, post_id):
        return self.get(f'posts/{post_id}')

    def create_post(self, post_data):
        return self.post('posts', post_data)

    def update_post(self, post_id, post_data):
        return self.put(f'posts/{post_id}', post_data)

    def delete_post(self, post_id):
        return self.delete(f'posts/{post_id}')

    # Comments
    def get_comments(self):
        return self.get('comments')

    def get_comment_by_id(self, comment_id):
        return self.get(f'comments/{comment_id}')

    def create_comment(self, comment_data):
        return self.post('comments', comment_data)

    def update_comment(self, comment_id, comment_data):
        return self.put(f'comments/{comment_id}', comment_data)

    def delete_comment(self, comment_id):
        return self.delete(f'comments/{comment_id}')

    # Albums
    def get_albums(self):
        return self.get('albums')

    def get_album_by_id(self, album_id):
        return self.get(f'albums/{album_id}')

    def create_album(self, album_data):
        return self.post('albums', album_data)

    def update_album(self, album_id, album_data):
        return self.put(f'albums/{album_id}', album_data)

    def delete_album(self, album_id):
        return self.delete(f'albums/{album_id}')

    # Photos
    def get_photos(self):
        return self.get('photos')

    def get_photo_by_id(self, photo_id):
        return self.get(f'photos/{photo_id}')

    def create_photo(self, photo_data):
        return self.post('photos', photo_data)

    def update_photo(self, photo_id, photo_data):
        return self.put(f'photos/{photo_id}', photo_data)

    def delete_photo(self, photo_id):
        return self.delete(f'photos/{photo_id}')
