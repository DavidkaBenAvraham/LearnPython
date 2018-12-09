from people import *
from elevator import *
import time
import db_elevator

Elevator.floor_group = 3
elevator = [] # list of elevators '''
passenger = [] # list of passengers '''


#создаем лифты
create_elevators(elevator , 3)



n = 0 #пока здесь число, но преполагается время с 8:00 до 17:00 (например)
while n < 40:
    get_passengers()
    n+=1




#db_elevator.conn



