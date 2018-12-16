
from passengers import *
from log import *
#import db_elevator
import threading

log.clear()

###############################################################################################################
#                               лифт
#       для нескольких
#elevator = []
#create_elevators(elevator , 1)
#el = Elevator()

#                               пассажир
# list of passengers '''
passenger = []


while True:
    # люди заходят не всегда, а с некоторым интервалом
    time.sleep(random.randint(1, 5)) # от одной до пяти секунд
    create_passenger(passenger)
    




