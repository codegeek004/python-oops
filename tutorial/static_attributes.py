class Customer:
    #this is static attribute. This is accessible within this class and instance objects only
    count = 0

    def __init__(self, name, contact):
        #these are instance attributes
        self.name = name
        self.contact = contact
        Customer.count += 1

    def display_user(self):
        print(f"Username: {username}, contact: {contact}")

c1 = Customer('ajay', '123')
c2 = Customer('yash', '456')
c3 = Customer('Nitin', '789')
print(Customer.count)
