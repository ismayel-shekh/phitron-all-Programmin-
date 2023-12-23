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
    def book_seats(self,id,row,cal):
        flag = False
        for show in self.show_list:
            if show[0] == id:
                flag == True
                self.seats[id][row][cal] = 1
        if flag == False:
            print('invalid id')
    def view_show_list(self):
        for show in self.show_list:
            print(f'ID {show[0]},movie: {show[1]},Time: {show[2]}')
    def vew_available_seats(self,id):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] != 1:
                    print(f"Row: {row}, col: {col}")
                else:
                    print('Already Booked!!!')
hall = Hall(6,6,1)
Star_cinema.entry_hall(hall)
hall.entry_show(100,'python','8.00 pm')
hall.entry_show(200,'CPP','11:00 pm')
print('\n--------------wellcome---------------\n')
while True:
    print(
          '1. view all show todey\n'
          '2. view available seats\n'
          '3. book ticket\n'
          '4. exit\n'
          )
    ch = int(input("enter option: "))
    if ch == 1:
        hall.view_show_list()
    if ch == 2:
        id = int(input('enter id to view available seats: '))
        hall.vew_available_seats(id)
    elif ch == 3:
        id = int(input('enter id to show available seats: '))
        seat = int(input('enter number of seats you book: '))
        for _ in range(seat):
            row = int(input('enter row: '))
            col = int(input('enter colum: '))
        hall.book_seats(id,row,col)
        print('ticket booked successfully!!')
    elif ch == 4:
        break

