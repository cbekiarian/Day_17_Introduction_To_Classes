class User:
    def __init__ (self, seat,username):

        self.seat = seat
        self.username = username
        self.follower = 0
        self.following = 0

    def follow(self,user):
        self.follower += 1
        user.following += 1

pog = User(1,"lording")
user_1 = User(2,"insano")

pog.follow(user_1)
pog.follow(pog)
print(pog.following)
print(pog.follower)
print(user_1.follower)
print(user_1.following)
