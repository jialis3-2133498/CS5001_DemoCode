from person import Person


def main():
    my_person1 = Person("Marge", 40)
    # Creating an object in Person calss
    my_person1.introduce_self()
    # access introduce_self method
    
    my_person2 = Person("Asteris the Gaul", 55)
    # Each object is seperate from each other
    # and methods can be accessed for this object
    my_person2.introduce_self()

    my_person3 = Person("Leta Orana", 25)
    my_person3.introduce_self()

    my_person1.befriend(my_person2)
    my_person1.befriend(my_person3)
    my_person1.introduce_self()

    my_person3.introduce_self()
    my_person2.introduce_self()


main()
