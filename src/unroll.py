class Person:
    DEAFULT_NAME="John Doe"

    def __init__(self,name=DEAFULT_NAME):
        self.name=name
        self.friends=[]

    def addFriend(self,other_person):
        self.friends.append(other_person)


def search_tree(person,name_to_find):
    for friend in person.friends:
        if friend.name==name_to_find:
            return friend
        friend2=search_tree(friend,name_to_find)
        if (friend2 is not None):
            return friend2
    return None

def unrolled_search(person,name_to_find):
    temp=[person]
    while (len(temp)>0):
        person=temp.pop(index=0)
        if person.name==name_to_find:
            return person
        temp.extend(person.friends)