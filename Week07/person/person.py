class Person:
    """
    A class representing a person
    """
    def __init__(self, name, age):
        """
        Construct a Person object
        """
        self.name = name
        self.age = age
        self.friends = []

    def get_name(self):
        return self.name

    def introduce_self(self):
        """
        Prints out self introduction
        """
        print(f"Hi! I'm {self.name} and I'm {self.age} years old.")
        self.introduce_friends()

    def introduce_friends(self):
        if (len(self.friends) > 0):
            print("My friends are:")
            for friend in self.friends:
                print(f"\t{friend.get_name()}")
        else:
            print("I like to work alone.")

    def befriend(self, new_friend):
        """
        Add friend to the friends list
        """
        self.add_friend(new_friend)
        new_friend.add_friend(self)

    def add_friend(self, new_friend):
        """
        Add friend to friends list
        """
        self.friends.append(new_friend)
