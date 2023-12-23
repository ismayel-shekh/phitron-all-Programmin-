# QA 9  Make the information of the classes as protected/private
# QA 7 replica system

class Star_Cinema:
    hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        self.hall_list.append(Hall(rows, cols, hall_no))

#QA 2
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no

#QA 3
    def entry_show(self, id='', movie_name='', time=''):
        self.__show_list.append((id, movie_name, time))
        seatInfo = []
        rowChar = 65
        for i in range(self.__rows):
            col =[]
            for j in range(self.__cols):
                col.append(f'{chr(rowChar)}{j}')
            seatInfo.append(col)
            rowChar += 1
        makeKey = {id: seatInfo}
        self.__seats.update(makeKey)

#QA 4
    def book_seats(self,customer_name,phone_num,show_id,seatList=[()]):
        for i in seatList:
            for get_id in self.__seats:
                if get_id == show_id:
                    self.__seats[get_id][i[0]][i[1]] = 'X'
        movieDetails = ()
        for i in self.__show_list:
            if i[0] == show_id:
                movieDetails = i
        customer_details = {'name': customer_name,'phone': phone_num,'show_id': show_id,'seatList': seatList,
                            'movieDetails': movieDetails}
        return customer_details

#QA 5
    def view_show_list(self):
        for i in self.__show_list:
            print('\t\tMovie Name: ',i[1], '\t\tShow Id: ', i[0], '\t\tTime: ', i[2])

   #QA 60.txt
    def view_available_seats(self,show_id):
        for k in self.__seats[show_id]:
            for j in k:
                print('\t',j,end=' ')
            print('\n')

        # QA 8 b

    def isValidId(self,show_id):
        for i in self.__show_list:
            if i[0] != show_id:
                pass
            else:
                return True
        return False

    #QA 8 c
    def isTicketValid(self, show_id, seatList=[()]):
        Booked = False
        for i in seatList:
            for get_id in self.__seats:
                if get_id == show_id:
                    if i[0] > self.__rows or i[1] > self.__cols or i[0] < 0 or i[1] < 0:
                        Booked = 2
                        return Booked
                    elif self.__seats[get_id][i[0]][i[1]] == 'X':
                        Booked = True
                        return Booked
        return Booked

    def movie_details(self,show_id):
        for index,i in enumerate(self.__show_list):
            if i[0] == show_id:
                print(f'\nMOVIE NAME : {self.__show_list[index][1]} '
                      f'\tMOVIE TIME : {self.__show_list[index][2]}')

sony = Star_Cinema()
sony.entry_hall(3, 5, 'Sony0')
sony.hall_list[0].entry_show('mor', 'Din the Day', '12 Nov 2022 10:00 AM')
sony.hall_list[0].entry_show('day', 'Rat the Day', '12 Nov 2022 03:00 PM')


while True:
    print('1.VIEW ALL SHOWS TODAY'
          '\n2.VIEW AVAILABLE SEATS'
          '\n3.BOOK TICKET')
    option = int(input('ENTER OPTION: '))
    if option == 1:
        print('\n')
        print('--------------------------------------------------------------------------------------------')
        sony.hall_list[0].view_show_list()
        print('--------------------------------------------------------------------------------------------')
        print('\n')
    elif option == 2:
        input_id = input('ENTER SHOW ID: ')
        check_id_validation = sony.hall_list[0].isValidId(input_id)
        if check_id_validation == True:
            sony.hall_list[0].movie_details(input_id)
            print("X for already Booked")

            l = len(sony.hall_list[0]._Hall__seats[input_id][0])
            for i in range(l):
                print('-------',end='')
            print('\n')
            sony.hall_list[0].view_available_seats(input_id)
            for i in range(l):
                 print('-------',end='')
            print('\n')
        else:
            print('\nGiven the Show Id is not exists.'
                  '\nPlease Give again in correct Show ID\n')
    elif option == 3:
        name = input('ENTER CUSTOMER NAME : ')
        phone_num = input('ENTER CUSTOMER PHONE NUMBER : ')
        show_id = input('ENTER SHOW ID : ')
        ticketQuantity = input('ENTER NUMBER OF TICKET : ')
        ticketList = []
        ticket = []

        for i in range(int(ticketQuantity)):
            seatNo = input('ENTER SEAT NO : ')
            seatNo=seatNo.upper()
            ticket.append(seatNo)
            row = ord(seatNo[0])-65
            col = int(seatNo[1])
            seat = (row, col)
            ticketList.append(seat)
        check_id_validation= sony.hall_list[0].isValidId(show_id)

        if check_id_validation == True:
            ticket_valid_booked = sony.hall_list[0].isTicketValid(show_id, ticketList)
            if ticket_valid_booked == False:
                customerBooking = sony.hall_list[0].book_seats(name, phone_num, show_id, ticketList)
                print('\n')
                print('******TICKET BOOKED SUCCESSFULLY!! ******')
                print( '-------------------------------------------------------------------------------------')
                print('NAME : ', name)
                print('PHONE NUMBER : ', phone_num)
                print('MOVIE NAME : ', customerBooking['movieDetails'][1],
                      '\tMOVIE TIME : ', customerBooking['movieDetails'][2])
                print('TICKETS : ', end=' ')
                for i in ticket:
                    print(i, end=' ')
                print('')
                print('Hall_No : Sony0')
                print( '-------------------------------------------------------------------------------------')
                print('\n')
            elif ticket_valid_booked == True:
                print('----------------------------------------------------')
                print('This ticket is already booked.'
                      '\nPlease try another')
                print('----------------------------------------------------')
            elif ticket_valid_booked == 2:
                print('----------------------------------------------------')
                print('This is not a valid ticket.'
                      '\nPlease try again')
                print('----------------------------------------------------')
        else:
            print('----------------------------------------------------')
            print('Given the Show Id is not exists.'
                  '\nPlease Give again in correct Show ID')
            print('----------------------------------------------------')
    else:
        print('Your input is not valid.'
              '\nPlease try again')