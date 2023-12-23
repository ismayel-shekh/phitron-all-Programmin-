# Q1
class Star_cinema:
    hall_list = []
    def entry_hall(self,row,cal,hall_no):
        self.hall_list.append(Hall(row,cal,hall_no))
class Hall(Star_cinema):
    def __init__(self,row,cal,hall_no) -> None:
        self.seats = []