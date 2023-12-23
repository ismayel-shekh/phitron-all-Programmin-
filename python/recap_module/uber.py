from abc import ABC, abstractmethod
class Ride_sharing:
    def __init__(self,company_name) -> None:
        self.company_name = company_name
        self.drivers = []
        self.riders = []
    def add_rider(self,rider):
        self.riders.append(rider)
    def add_driver(self,driver):
        self.drivers.append(driver)
    def __repr__(self) -> str:
        return f'{self.company_name} has {len(self.riders)} riders and {len (self.drivers)} Drivers '

class user(ABC):
    def __init__(self,name, email,nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid 
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Driver(user):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
    def display_profile(self):
        print(f'Driver name is {self.name} and mail is {self.email}')
class Rider(user):
    def __init__(self, name, email, nid,current_location) -> None:
        super().__init__(name, email, nid)
        self.current_ride = None
        self.current_location = current_location
    def display_profile(self):
        print(f'Rider name is {self.name} and mail is {self.email}')

    def ride_request(self,uber,destination):
        print('loking for ride')
        if not self.current_ride:
            op = Ride_Matching(uber.drivers)
            result = op.has_driver(self,destination)
            print('your result is',result)
            self.current_ride = result
            return True
        else:
            return False

class Ride:
    def __init__(self,start_location,end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
    def start_ride(self):
        pass
    def end_ride(self):
        pass
    def __repr__(self) -> str:
        return(f'start from {self.start_location} to {self.end_location}')

class Ride_Matching:
    def __init__(self,drivers) -> None:
        self.drivers = drivers
    def has_driver(self,rider,destionation):
        if len(self.drivers) > 0:
            ride = Ride(rider.current_location,destionation)
            return ride
        else:
            return "sorry, driver Not Found!"
uber = Ride_sharing('Uber')
alice = Driver("alish",'alaice@gmeil.com',12346,"Gazipur")
sakib = Rider('sakib','sakib@gmail.com',123,'rajandropur')
uber .add_driver(alice)
uber.add_rider(sakib)
if sakib.ride_request(uber,"dhaka"):
    print('traveling')
else:
    print("No ride found")