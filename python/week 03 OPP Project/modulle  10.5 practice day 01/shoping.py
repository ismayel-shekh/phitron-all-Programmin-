class Customer:
    def __init__(self, customar_name, customer_email, customer_password) -> None:
        self.customar_name = customar_name
        self.customar_email = customer_email
        self.customer_password = customer_password
    def __repr__(self) -> str:
        return f'customar name: {self.customar_name}\n customar email: {self.customar_email}\n customar password: {self.customer_password}'
korim = Customer('ismayel','ismayel@gamil.com',12345)
print(korim)
class Sellers:
    def __init__(self,se) -> None:
        