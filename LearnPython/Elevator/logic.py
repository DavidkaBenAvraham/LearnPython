from passenger import *
from elevator import *
import db_elevator
import threading



#создаем лифты
create_elevators(elevator , 3)



#n = 0 #пока здесь число, но преполагается время с 8:00 до 17:00 (например)
#while n < 40:
#    get_passengers()
#    n+=1




###############################################################################################################
# создаем два потока
# пассажир
# лифт


# https://www.ibm.com/developerworks/ru/library/l-python_part_9/index.html

#import threading
#import time
#def clock(interval):
#    while True:
#        print("The time is %s" % time.ctime())
#        time.sleep(interval)
#t = threading.Thread(target=clock, args=(15,))
#t.daemon = True
#t.start()

#threading_passengers = threading.Thread(target=start_passengers , args=(passenger))
#threading_passengers.start()


p = PassThread(passenger)
p.setName(Passenger.pass_num - 1)
p.start()
print("PassThread =" , p.getName())

#######################################################################################################

#db_elevator.conn



