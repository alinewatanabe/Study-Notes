class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

# user_2 = User()
# user_2.id = "002"
# user_2.username = "Yugo"

user_1 = User("001", "Lin")
user_2 = User("002", "Yugo")

user_1.follow(user_2)

print(user_1.following)
print(user_2.followers)