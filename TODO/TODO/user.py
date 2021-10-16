
class User:
    __user = None

    def __init__(self,name) -> None:
        self.name = name

    def login(username):
        User.__user = User(username)

    def isLoged():
        return User.__user != None
    
    def logout():
        User.__user = None

    def getUser():
        return User.__user
