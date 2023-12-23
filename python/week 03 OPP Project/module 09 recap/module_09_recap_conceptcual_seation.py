from abc import ABC, abstractmethod
class Ride_Sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.drivers = []
        self.riders = []
    def add_riders(self,rider):
        self.riders.append(rider)
    def add_drivers(self,driver):
        self.drivers.append(driver)
    def __repr__(self) -> str:    # __repr__ it name dunder mathod
        return f'{self.company_name} has {len(self.riders)} riders and {len(self.drivers)} drivers'
    

class User(ABC):
    def __init__(self,name,email,nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Driver(User):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
    def display_profile(self):
        print(f'Driver name is{self.name} and mail is {self.email}')

class Rider(User):
    def __init__(self, name, email, nid,current_location) -> None:
        self.current_ride = None
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        print(f'Rider name is {self.name} and mail is {self.email}')
    def ride_request(self,uber,destination):
        if not self.current_ride:
            ob = Ride_matchig(uber.drivers)
            res = ob.has_driver(self,destination)
            print("your result is ,",res)
            self.current_ride = res
            return True
        else:
            return False
class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
    def start_rider(self):
        pass
    def end_ride(self):
        pass
    def __repr__(self) -> str:
        return f"start from{self.start_location} to {self.end_location}"
    
class Ride_matchig:
    def __init__(self,drivers) -> None:
        self.drivers = drivers
    def has_driver(self,sakib,destination):
        if len(self.drivers) > 0:
            ride = Ride(sakib.current_location,destination)
            return ride
        else:
            return "sorry, driver not found"




uber = Ride_Sharing('UBER')

alice = Driver('alice','alice@gmail.com',12345,'Chittagong 1')
sakib = Rider('Sakib','sakib@gmail.com',1236,'Chittagong 2')

uber.add_drivers(alice)
uber.add_riders(sakib)
if sakib.ride_request(uber,'Dhaka'):
    print("traveling...")

else: 
    print("No ride found")
