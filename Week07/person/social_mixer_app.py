from person import Person


def main():
    my_person1 = Person("Marge", 40)
    my_person1.introduce_self()

    my_person2 = Person("Asterix the Gaul", 55)
    my_person2.introduce_self()

    my_person3 = Person("Leia Organa", 25)
    my_person3.introduce_self()

    my_person1.befriend(my_person2)
    my_person1.befriend(my_person3)
    my_person1.introduce_self()

    my_person3.introduce_self()


main()
