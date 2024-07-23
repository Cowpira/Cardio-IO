# defining class client
from dataclasses import dataclass


@dataclass
class Client(object):
    # defining client attributes
    name: str
    result_status: bool
    file_name: str
    hr_graph: str
    result_date: str
    heart_rate: int
    rms_value: float
    rms_accuracy: int
    rms_error: int


# define a list of clients
client_list = []

cli1 = Client('John Rave', True, 'None', 'John Rave_graph.png', 'January 7, 2024', 84, 103.06, 88, 3)
client_list.append(cli1)
cli2 = Client('Wanda Smith', False, 'None', 'Wanda Smith_graph.png', 'January 14, 2024', 79, 843.15, 90, 1)
client_list.append(cli2)
cli3 = Client('Steve Long', False, 'None', 'Steve Long_graph.png', 'February 2, 2024', 90, 112, 77, 10)
client_list.append(cli3)
cli4 = Client('Simone Cole', True, 'Simone Cole_07_20_2024.pdf', 'Simone Cole_graph.png',
              'March 7, 2024', 77, 96.13, 100, 0)
client_list.append(cli4)
cli5 = Client('Shawn Pat', True, 'Shawn Pat_07_12_2024.pdf', 'Shawn Pat_graph.png',
              'April 9, 2024', 92, 98.26, 94, 6)
client_list.append(cli5)
cli6 = Client('Sarah Jones', False, 'Sarah Jones_07_12_2024.pdf', 'Sarah Jones_graph.png',
              'May 11, 2024', 100, 117, 65, 25)
client_list.append(cli6)
cli7 = Client('Ray Allen', False, 'Ray Allen_07_20_2024.pdf', 'Ray Allen_graph.png', 'May 15, 2024', 104, 82.23, 75, 12)
client_list.append(cli7)
cli8 = Client('Maria Hall', False, 'None', 'Maria Hall_graph.png', 'June 22, 2024', 95, 100.23, 92, 6)
client_list.append(cli8)
cli9 = Client('Brian Scott', True, 'Brian Scott_07_12_2024.pdf', 'Brian Scott_graph.png',
              'July 10, 2024', 75, 89.90, 93, 7)
client_list.append(cli9)
