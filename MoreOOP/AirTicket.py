##Airline Ticket

class AirTicket (object):
     

    def __init__(self, name, depart, arrive, tickClass, price):
        self.name = name
        self.departAirport = depart
        self.arriveAirport = arrive
        self.ticketClass = tickClass
        self.price = price


    def __str__(self):
        out = self.name + " leaving from " + self.departAirport
        out = out + " traveling to " + self.arriveAirport
        out = out + " with class " + self.ticketClass + " costing " + str(self.price)
        return out


    def changeTicket(self, newClass, newPrice):
        self.ticketClass = newClass
        self.price = newPrice



def tester():
    ticket1 = AirTicket("Sam Spade", "DSM", "ORD", "business", 1315.12)
    ticket2 = AirTicket("Joe Doe", "ALT", "JFK", "economy", 425.25)
    print(ticket1)
    print(ticket2)
    ticket1.changeTicket("first", 5000.00)
    print(ticket1)

tester()
