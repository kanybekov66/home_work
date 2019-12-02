class Contact:                                                 # создан класс "Contact"
    def __init__(self, name, last_name, number):
        self.name = name
        self.last_name = last_name
        self.number = number


class ContactList:                                              # создан класс ContactList
    def __init__(self):
        self.contacts_list = []


    def add_contact(self, contact):                             # метод добавляет объект класса Contact в contacts_list
        self.contact = contact
        self.contacts_list.append(self.contact)


    def search_contact(self, contact):                          # метод находит объект класса Contact в contact_list
        for i in self.contacts_list:
            if i == contact:
                print("contact is found: ", i)



    def remove_contact(self, contact):                          # метод удаляет из contacts_list объект класса Contact
        for i in self.contacts_list:
            if i == contact:
                self.contacts_list.remove(contact)
                print(contact, " deleted")





stella = Contact("Stella", "Artois", 202020)
albina = Contact("Al'bina", "Alymkulova", 303030)
mukha = Contact("Mukhtar", "Kasymov", 404040)


contacts = ContactList()
contacts.add_contact(stella)
contacts.add_contact(albina)
contacts.add_contact(mukha)

contacts.search_contact(mukha)
contacts.remove_contact(mukha)

