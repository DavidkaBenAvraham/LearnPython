
#from elevators import *
#from passengers import *
import elevators, passengers, log
import db_elevator
import threading



###############################################################################################################
#                               лифт
#       для нескольких
#elevator = []
#create_elevators(elevator , 1)



el = create_elevator()

# пассажир
# list of passengers '''
passenger = []
while True:
    # люди заходят не всегда, а с некоторым интервалом
    time.sleep(random.randint(1, 5)) # от одной до пяти секунд
    create_passenger(passenger , el)




