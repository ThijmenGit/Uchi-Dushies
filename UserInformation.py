class UserInformation:
    def __init__(self):
        self.name = None
        self.data = ["Manon Heinrich", "Luke Boers"]

    def login(self):
        print("Welcome to the Investment Game, please provide your")
        firstname = input("Firstname: ")
        lastname = input("Lastname: ")
        fullname = firstname + " " + lastname
        print(fullname)
        if fullname not in self.data:
            self.new_user()
        else:
            self.recurring_user()

    def new_user(fullname):
        print("Welcome to the game. Get ready to become the ultimate sensei")

    def recurring_user(fullname):
        print("Welcome back")


if __name__=="__main__":
    user = UserInformation()
    user.login()

