import logging


class UserService:
    def __init__(self, api_client):
        self.api_client = api_client

    def get_fancode_users(self):
        """Filters users from the 'FanCode' city based on lat and long."""
        logging.info("Fetching users from the API.")
        users = self.api_client.get_users()
        fancode_users = []
        for user in users:
            lat = float(user['address']['geo']['lat'])
            lng = float(user['address']['geo']['lng'])
            if -40 <= lat <= 5 <= lng <= 100:
                fancode_users.append(user)
        logging.info(f"Filtered {len(fancode_users)} users from 'FanCode'.")
        return fancode_users

    def get_user_completed_todo_percentage(self, user_id):
        """Calculates completed todos percentage for a user."""
        logging.info(f"Fetching todos for user {user_id}.")
        todos = self.api_client.get_todos()
        user_todos = [todo for todo in todos if todo['userId'] == user_id]
        completed_todos = [todo for todo in user_todos if todo['completed']]

        if len(user_todos) == 0:
            logging.warning(f"User {user_id} has no todos.")
            return 0
        completion_percentage = (len(completed_todos) / len(user_todos)) * 100
        logging.info(f"User {user_id} completed {completion_percentage:.2f}% of their todos.")
        return completion_percentage

    def is_user_completing_more_than_half_tasks(self, user_id):
        """Returns True if the user completed more than 50% of their todos."""
        return self.get_user_completed_todo_percentage(user_id) > 50
