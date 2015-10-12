phonebook = {'Bob':12314}

def create (name, phone):
    phonebook['name'] = phone
    print name, phonebook[name]
    
def read (name):
    if phonebook.has_key('name'):
        print phonebook[name]
    else:
        raise ValueError ('Contact not found')

def update (name, phone):
    if phonebook.has_key('name'):
        phonebook['name'] = phone
    print name, phonebook[name]

def delete (name):
    if phonebook.has_key('name'):
        phonebook.popitem ['name']
    else:
        raise ValueError ('Contact not found')

while True:
    act = raw_input('Enter your command (CRUD) ')
    if act in 'Cc':
        name = str(raw_input('enter new name '))
        phone = str(raw_input('enter new phone '))
        create (name, phone)
        
    elif act in 'Rr':
        name = str(raw_input('name? '))
        read (name)

    elif act in 'Uu':
        name = str(raw_input('name? '))
        phone = str(raw_input('enter new phone '))
        update (name, phone)

    elif act in 'Dd':
        name = str(raw_input('name? '))
        delete (name)

    elif act in 'Qq':
        break
print phonebook
