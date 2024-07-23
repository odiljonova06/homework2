from masala1 import String 
from masala2 import Intger
from masala3 import Mylist
from masala4 import Boolen
from masala5 import Float





class User:
    username = String()
    first_name = String()
    last_name = String()
    age = Intger()
    groups = Mylist()
    status = Boolen()
    rating = Float()

    def __init__(self, username: str, first_name: str, last_name: str, age: int, groups: list, status: bool, rating: float):
        self.username = username 
        self.first_name = first_name
        self.last_name = last_name 
        self.age = age 
        self.groups = groups 
        self.status = status 
        self.rating = rating 

user = User("odljnvas", "Odiljonova", "Robiya", 18, [3,4], True, 5.5)
print (user)


