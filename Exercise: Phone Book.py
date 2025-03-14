phonebook = {}

phonebook["Andrew"] = '6466328432'
phonebook["Adam"] = '9178332964'
phonebook["William"] = '3194556495'
phonebook["Chuzz"] = '9298773373'
phonebook["Empluzz"] = '9293336421'

ask = input("Enter a name to lookup")

if ask in phonebook:
    print(phonebook[ask])
else:
    print("This number is not in the phonebook")