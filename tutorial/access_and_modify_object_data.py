from datetime import datetime
class User:
    def __init__(self, username, email):
        self.username = username
        self._email = email
        # _ makes a data atrribute protected but you can still access this although this is considered a bad practice. 
        #If you want to make the attribute strictly inaccessible you can __ which makes the attribute private and inaccessible. 

    #def get_email(self):
    #    #return self._email
    #    return self._email.lower().strip()
    
    #def set_email(self, email):
    #    if '@' and '.' in email:
    #        self._email = email
    #    else:
    #        print("Invalid Email")
    #This is traditional way of getting and setting data in object oriented programming but python has its own way of doing this --> @property

    @property
    def email(self):
        print('email accessed')
        return self._email

    @email.setter
    def email(self, new_email):
        if '@' and '.' in new_email:
            self._email = new_email
        else:
            print('Invalid Email')

    @email.deleter
    def email(self):
        del self._email

user1 = User('codegeek004', 'codegeek004@gmail.com')
print(user1.email)
user1.email = "abc@gmail.com"
print(user1.email)
del user1.email
print(user1.email)
