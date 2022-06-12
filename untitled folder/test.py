import names
import random, string
from random_address import real_random_address
#print()

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

emailProviders = [ "@gmail.com", "@yahoo.com", "@apple.com", "@proton.com", "@customemail.com"]


for i in range(1):
    firstname = names.get_first_name()
    lastname = names.get_last_name()
    items = ["", str(random.randrange(1,999))]
    random_item = random.choice(items)
    random_email = random.choice(emailProviders)
    random_address = real_random_address()
    #print(random_item)
    mydict = {
            "Username": firstname + lastname,
            "Password": randomword(10),
            "email": firstname + "." + lastname + random_item + random_email,
            "Name": firstname,
            "Surname": lastname,
            "Location": {
                "Address": [
                    random_address["address1"],
                    random_address["address2"]
                ],
                "Postcode": random_address["postalCode"],
                "City": random_address["state"],
                "Country": "United States"
            }
    }
    
    print(mydict)
    
            