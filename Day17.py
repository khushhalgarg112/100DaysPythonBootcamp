'''class Man:
    def fun(self): # we have to add a self argument in the  function else we got an error
        print("HI")

child = Man()
child.fun()'''


# OOPS 
'''class User:
    # name = ""
    # id  = 0
    def __init__(self,id,name):
        self.name = name
        self.id = id
        self.followers= 0 # this is also an default attribute
        self.following = 0

    def follow(self,user):
        # self.followers = 4 # here we have changed value of followers
        user.followers += 1
        self.following +=1

user_1 = User(1,"Khushhal")
user_2 = User(2,"Raju")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
'''

