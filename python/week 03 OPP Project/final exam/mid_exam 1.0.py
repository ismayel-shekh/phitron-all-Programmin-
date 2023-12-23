class Star_cinema:
    __hall_list = []
    @classmethod
    def entry_hall(self,hall):
        self.__hall_list.append(hall)
class Hall(Star_cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats = {}
        self.rows =rows
        self.cols = cols
        self.hall_no = hall_no
        self.show_list = []
    def entry_show(self,id,movie_name,time):
        movie = (id,movie_name,time)
        self.show_list.append(movie)
        self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
    def book_seats(self, id, row, col):
        flag = False
        for show in self.show_list:
            if show[0] == id:
                flag = True 
                self.seats[id][row][col] = 1
                print(f'SEAT {row , col} BOOKED')
        if not flag:
            print('INVALID ID')

    def view_show_list(self):
        for show in self.show_list:
            print(f'MOVIE NAME: {show[1]} SHOW ID: {show[0]} TIME: {show[2]}')

    def vew_available_seats(self, id):
        if id not in self.seats:
            print(f'Show ID {id} does not exist.')
            return

        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] != 1:
                    print(f"Row: {row}, Col: {col}")
                else:
                    print('Already Booked!!!')
hall = Hall(6,6,1)
Star_cinema.entry_hall(hall)
hall.entry_show(100,'PYTHON','8.00 pm')
hall.entry_show(200,'JAVA','11:00 pm')
print('\n--------------WELLCOEM TO PYTHON CHINEMA HALL---------------\n')
while True:
    print(
          '1. VIEW ALL SHOW TODAY\n'
          '2. VIEW AVAILABLE SEATS\n'
          '3. BOOK TICKET\n'
          '4. EXIT\n'
          )
    ch = int(input("ENTER OPTION: "))
    if ch == 1:
        print('________________TODAY AVAILABLE SHOW____________')
        hall.view_show_list()
    if ch == 2:
        id = int(input('ENTER SHOW ID: '))
        hall.vew_available_seats(id)

    elif ch == 3:
        while True:
            id = int(input('ENTER SHOW ID TO BOOK TICKET: '))
            if id not in [show[0] for show in hall.show_list]:
                print('INVALID ID. Please enter a valid show ID.')
            else:
                break

        seat = int(input('NUMBER OF TICKET?: '))
        for _ in range(seat):
            row = int(input('enter row: '))
            col = int(input('enter column: '))
            hall.book_seats(id, row, col)
        # print('Tickets booked successfully!!')
    elif ch == 4:
        break

