from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.user_repo = UserRepository

    def get_all_users(self):
        return [user.to_dict() for user in self.user_repo.get_all()]

    def get_user_by_id(self, user_id):
        user = self.user_repo.get_by_id(user_id)
        return user.to_dict() if user else None

    def create_user(self, user_data):
        return self.user_repo.create(user_data).to_dict()

    def delete_user(self, user_id):
        return self.user_repo.delete(user_id)