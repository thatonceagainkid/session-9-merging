import unroll as ur

print("Hello!, Good Morning!")

person=ur.Person()
chris=ur.Person("Chris Arnold")
person.addFriend(chris)

erika=ur.Person("Erika Rosero")
person.addFriend(erika)

print(person.friends)

