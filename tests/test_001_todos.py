from main.service.user_service import UserService
from tests.base_test import BaseTest


class TestFancodeUsersTodos(BaseTest):

    def test_fancode_users_have_more_than_half_todos_completed(self):
        """
        All the users of City `FanCode` should have more than half of their todos task completed
        """
        user_service = UserService(self.client)
        fancode_users = user_service.get_fancode_users()

        for user in fancode_users:
            assert user_service.is_user_completing_more_than_half_tasks(user['id']), \
                f"User {user['id']} from FanCode city has less than 50% completed tasks."
