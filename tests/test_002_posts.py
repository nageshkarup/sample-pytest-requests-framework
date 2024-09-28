from main.service.post_service import PostService
from main.service.user_service import UserService
from tests.base_test import BaseTest


class TestPosts(BaseTest):

    def test_users_have_more_than_3_posts(self):
        """Test to ensure that users have more than 3 posts."""
        post_service = PostService(self.client)
        user_service = UserService(self.client)

        fancode_users = user_service.get_fancode_users()

        for user in fancode_users:
            assert post_service.user_has_more_than_n_posts(user['id'], 3), \
                f"User {user['id']} has 3 or fewer posts."
