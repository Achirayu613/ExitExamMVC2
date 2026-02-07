import csv

class AuthController:
    def __init__(self):
        self.users = []
        self.is_admin = False
        self.load_users()

    def load_users(self):
        with open("data/users.csv", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            self.users = list(reader)

    def login(self, username, password):
        for u in self.users:
            if u["username"] == username and u["password"] == password:
                self.is_admin = (u["role"] == "admin")
                return True
        return False
