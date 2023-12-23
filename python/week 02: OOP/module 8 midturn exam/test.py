class Star_Cinema:
    __hall_list=[]
    @classmethod
    def entry_hall(self,hall):
        self.__hall_list.append(hall)
class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no):
        
        self.seats={}
        self.rows=rows
        self.cols=cols
        self.hall_no=hall_no
        self.show_list=[]
        # hall=Hall(rows,cols,hall_no)
        # Star_Cinema.entry_hall(hall)
    
    def entry_show(self,id,movie_name,time):
        info=(id,movie_name,time)
        self.show_list.append(info)
        self.seats[id]=[[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def book_seats(self,id,row,col):
        flag=False
        for show in self.show_list:
            if show[0]==id:
                flag=True
                self.seats[id][row][col]=1   
        if flag==False:
            print('Invalid ID')
                                    
                
    
    def view_show_list(self):
        for show in self.show_list:
            print(f'ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}')
           

    def view_available_seats(self,id):
        print('started')
        for row in range(self.rows):
            for col in range(self.cols):
                if self.seats[id][row][col] != 1:
                    print(f"Row: {row}, Col: {col}")  
                else:
                    print('Already Booked!!!')


hall=Hall(7,7,1)
Star_Cinema.entry_hall(hall)
hall.entry_show(110,'Jawan','11:00 AM')
hall.entry_show(220,'Leo','2:00 PM')
while True:
    print("1. VIEW ALL SHOW TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK TICKET")
    print("4. Exit")
    ch = int(input("Enter option: "))
    if ch==1:
        hall.view_show_list()
    elif ch==2:
        id=int(input('Enter show ID to view Available seats: '))
        hall.view_available_seats(id)
    elif ch==3:
        id=int(input('Enter show ID to view Available seats: '))
        
        seat=int(input("Enter number of seats to book: "))
        
        booking=[]
        for _ in range(seat):
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            
        hall.book_seats(id,row,col)
        print('Ticket Booked Successfully!!!')
    elif ch==4:
        break

