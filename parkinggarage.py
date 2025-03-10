class Parking():

    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.currentTicket = {}

                        
    def payTicket(self):
        ticket = int(input('what is your ticket number? '))
        if self.currentTicket[ticket] == 'paid':
            print('You have paid, Thank you have a nice day!')
        else:
            pay = input('would you like to pay? (Y/N))').upper()
            if pay.upper() == 'Y':
                print('Thank you, please exit')
                self.currentTicket[ticket] = 'paid'
                self.parkingSpaces.append(ticket)
                self.tickets.append(ticket)
                print("your ticket status is: ", self.currentTicket[ticket])
            else:
                print('please pay to exit')
                self.payTicket()
                
    def park(self):
        while True:
            select = input("would you like to park/pay/exit or quit ? ").lower()
            if select == 'park':
                self.getTicket()
            elif select == 'pay':
                self.payTicket()
            elif select == 'exit':
                self.leaveGarage("fromExit")
            elif select == 'quit':
                break
            else:
                print("would you like to park/pay/exit or quit ? ").lower()

    def leaveGarage(self):
        ticket = int(input('enter your ticket number? '))
        if self.currentTicket[ticket] == 'paid':
            print(f'your ticket {ticket} is paid, have a good day')
        else:
            print(f'your ticket is unpaid, please pay your ticket number {ticket}')
            self.payTicket()
            

car1 = Parking()
car1.park()
