class User:
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0

    def descibe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} username is {self.username} and their age is {self.age}.")

    def greet_user(self):
        print(f"Greetings, {self.first_name.title()}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, age):
        """Initializes Admins"""
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges() # Adding class to the Admin attribute

    def show_privileges(self):
        print(f"Privileges for {self.first_name.title()}: ")
        for privileges in self.privileges:
            print(f"  - {privileges}")

class Privileges:
    """A class to store admin privileges"""
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("Privileges: ")
        if self.privileges:
            for privileges in self.privileges:
                print(f"  - {privileges}")
        else:
            print("This user has no priviledges")