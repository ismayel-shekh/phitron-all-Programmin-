class star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls,hall):
        cls._hall_list.append(hall)

    def __init__(self,hall_no,rows,cols) -> None:
        new_hall = Hall(hall_no,rows,cols)
        self.entry_hall(new_hall)
    
class Hall:
    def __init__(self,hall_no,rows,cols) -> None:
        self._seats = []
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        self._initialize_seats()

    def _initialize_seats(self):
        for _ in range(self._rows):
            row =["free"for _ in range(self._cols)]
            self._seats.append(row)
    
    def entry_show(self,show_id,movie_name,time):
        show_info = (show_id,movie_name,time)
        self._show_list.append(show_info)
    
    def book_seats(self,show_id,seat_list):
        if show_id not in [show[0] for show in self._show_list]:
            raise ValueError("invalid show ID")
        
        for row,col in seat_list:
            if(1 <= row <= self._rows and 1 <= col <= self._cols and self._seats[row - 1][col - 1] == "free"):
                self._seats[row - 1][col -1] = "Booked"
            else:
                raise ValueError("Invalid seat selection or seat already booked")
    
    def view_show_list(self):
        return self._show_list
    
    def  view_available_seats(self,show_id):
        if show_id not in [show[0] for show in self._show_list]:
            raise ValueError("invalid show ID")
        available_seats = []
        for i in range(self._rows):
            for j in range(self._cols):
                if self._seats[i][j] == "free":
                    available_seats.append((i+1, j+1))
        return available_seats
    
cinema = star_Cinema(1, 5, 5)
cinema._hall_list[0].entry_show("jamuna", "king kong", "15:00")
cinema._hall_list[0].book_seats("jamuna", [(1, 1), (2, 2), (3, 3)])
print(cinema._hall_list[0].view_show_list())
print(cinema._hall_list[0].view_available_seats("jamuna"))
