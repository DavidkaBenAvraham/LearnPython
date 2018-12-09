from passenger import *
from elevator import *
import db_elevator
import threading



# ####################################
#         ЛОГ
log = open('text.txt', 'w')


###############################################################################################################
#                               лифт
#       для нескольких
#elevator = []
#create_elevators(elevator , 1)





# https://www.ibm.com/developerworks/ru/library/l-python_part_9/index.html
###############################################################################################################
# пассажир
while True:
    # люди заходят не всегда, а с некоторым интервалом
    time.sleep(random.randint(1, 5)) # от одной до пяти секунд
    start_passengers(passenger)




