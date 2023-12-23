class Star_Cinema:
    hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        hall = Hall(rows, cols, hall_no)
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

    def entry_show(self, id='', movie_name='', time=''):
        show_info = (id, movie_name, time)
        self.__show_list.append(show_info)
        seats = [['O' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seats

    def book_seats(self, customer_name, phone_num, show_id, seatList=[()]):
        if show_id in self.__seats:
            for seat in seatList:
                row, col = seat
                if 0 <= row < self.__rows and 0 <= col < self.__cols:
                    if self.__seats[show_id][row][col] == 'O':
                        self.__seats[show_id][row][col] = 'X'
                    else:
                        return "Seat already booked"
                else:
                    return "Invalid seat"
            movie_details = self.get_show_info(show_id)
            customer_details = {
                'name': customer_name,
                'phone': phone_num,
                'show_id': show_id,
                'seatList': seatList,
                'movieDetails': movie_details
            }
            return customer_details
        else:
            return "Show not found"

    def view_show_list(self):
        for show in self.__show_list:
            print(f"Show ID: {show[0]}\tMovie Name: {show[1]}\tTime: {show[2]}")

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            for row in self.__seats[show_id]:
                for seat in row:
                    print(seat, end=' ')
                print()
        else:
            print("Show not found")

    def get_show_info(self, show_id):
        for show in self.__show_list:
            if show[0] == show_id:
                return show
        return None

    def is_valid_id(self, show_id):
        return show_id in [show[0] for show in self.__show_list]

    def is_ticket_valid(self, show_id, seatList=[]):
        if show_id not in self.__seats:
            return "Show not found"
        for seat in seatList:
            row, col = seat
            if 0 <= row < self.__rows and 0 <= col < self.__cols:
                if self.__seats[show_id][row][col] == 'X':
                    return "Seat already booked"
            else:
                return "Invalid seat"
        return True

    def movie_details(self, show_id):
        show = self.get_show_info(show_id)
        if show:
            print(f"Movie Name: {show[1]}\tTime: {show[2]}")

sony = Star_Cinema()
sony.entry_hall(3, 5, 'Table')
sony.hall_list[0].entry_show('mor', 'King Kong', '12 Nov 2022 10:00 AM')
sony.hall_list[0].entry_show('day', 'Monstar', '12 Nov 2022 03:00 PM')

while True:
    print('1. VIEW ALL SHOWS TODAY\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET')
    option = int(input('ENTER OPTION: '))

    if option == 1:
        print('\n')
        sony.hall_list[0].view_show_list()
        print('\n')
    elif option == 2:
        input_id = input('ENTER SHOW ID: ')
        check_id_validation = sony.hall_list[0].is_valid_id(input_id)
        if check_id_validation:
            sony.hall_list[0].movie_details(input_id)
            print("X for already Booked")
            l = len(sony.hall_list[0]._Hall__seats[input_id][0])
            for _ in range(l):
                print('-------', end='')
            print('\n')
            sony.hall_list[0].view_available_seats(input_id)
            for _ in range(l):
                print('-------', end='')
            print('\n')
        else:
            print('\nGiven Show ID does not exist. Please provide a correct Show ID.\n')
    elif option == 3:
        name = input('ENTER CUSTOMER NAME: ')
        phone_num = input('ENTER CUSTOMER PHONE NUMBER: ')
        show_id = input('ENTER SHOW ID: ')
        ticket_quantity = input('ENTER NUMBER OF TICKETS: ')
        ticket_list = []
        ticket = []
        for _ in range(int(ticket_quantity)):
            seat_no = input('ENTER SEAT NO: ')
            seat_no = seat_no.upper()
            ticket.append(seat_no)
            row = ord(seat_no[0]) - 65
            col = int(seat_no[1])
            seat = (row, col)
            ticket_list.append(seat)
        check_id_validation = sony.hall_list[0].is_valid_id(show_id)
        if check_id_validation:
            ticket_valid_booked = sony.hall_list[0].is_ticket_valid(show_id, ticket_list)
            if ticket_valid_booked == True:
                customer_booking = sony.hall_list[0].book_seats(name, phone_num, show_id, ticket_list)
                if isinstance(customer_booking, dict):
                    print('\n****** TICKET BOOKED SUCCESSFULLY! ******\n')
                    print('NAME:', name)
                    print('PHONE NUMBER:', phone_num)
                    print('MOVIE NAME:', customer_booking['movieDetails'][1])
                    print('MOVIE TIME:', customer_booking['movieDetails'][2])
                    print('\nTICKETS:', end=' ')
                    for ticket_seat in ticket:
                        print(ticket_seat, end=' ')
                    print('\nHall_No:', sony.hall_list[0]._Hall__hall_no)
                    print('\n')
                else:
                    print(f'\n{customer_booking}\n')
            else:
                print(f'\n{ticket_valid_booked}\n')
        else:
            print('\nGiven Show ID does not exist. Please provide a correct Show ID.\n')
    else:
        print('\nYour input is not valid. Please try again.')
