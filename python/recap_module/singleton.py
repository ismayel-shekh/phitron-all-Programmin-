#singleton --> only single instance
class singleton:
    __instance  = None
    def __init__(self) -> None:
        if singleton.__instance is None:
            singleton.__instance = self
        else:
            raise Exception('this is singleton. already have an instance')
    @staticmethod
    def get_instance():
        if singleton.__instance is None:
            singleton()
        return singleton.__instance
first = singleton.get_instance()    
print(first)
second = singleton.get_instance()
print(second)
last = singleton()