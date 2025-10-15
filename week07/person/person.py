class Person:
    """
    A class representing a person
    """
    def __init__(self, name, age):  # this is a method, not function
        # because it is inside a class
        # __init__ is a constructor, can create a new object
        # In this example, it is creating a new person
        # In the parameters, self means object itself
        """
        Construct a Person object
        """
        self.name = name
        # .name is an attribute of the object, same for the age
        self.age = age
        self.friends = []
        # Just initialize it as an empty value for every objects

    def get_name(self): 
        # This access another object
        # self means another object
        return self.name

    def introduce_self(self):  # Alaways to include self as the param
        # This is a method
        """
        Print out the object's introduction
        """
        print(f"Hi, I am {self.name} and I am {self.age} years old")
        # self is a global variable in this class, and all other methods
        # can access self.
        self.introduce_friends()
        
    def introduce_friends(self):
        """
        Helfper method
        """
        if (len(self.friends) > 0):
            print("My friends are:")
            for friend in self.friends:
                print(f"{friend.get_name()}")
        else:
            print("I have no friends")

    def befriend(self, new_friend):
        """
        Add a friend to friends list
        """
        self.add_friend(new_friend)
        new_friend.add_friend(self)

    def add_friend(self, new_friend):
        """
        Add friend to friends list
        """
        print(f"{self.name} befriending {new_friend.name}")
        self.friends.append(new_friend)

    
