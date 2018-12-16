import random
import log
import datetime
import time
import threading
import logic

from elevators import *


#Elevator = elevators.Elevator()
if __name__ == "__main__":
    pass

class Passenger:

    passenger_number = 1
    required_floor = 0 
    current_floor = 0
    floor_group = 0 # 0: 1 - 33; 2 - 34-66; 3 - 67-99
    direction = 0 #0 - stopped; "1" - up; "-1" - down
    #time = today.strftime("%Y-%m-%d %H:%M:%S")
    time = datetime.datetime.today()


    def __init__(self , current_floor = 0 , required_floor = 0):

        self.direction = 1 if current_floor < required_floor else -1
        self.passenger_number = Passenger.passenger_number
        self.current_floor = current_floor
        self.required_floor = required_floor
        
        self.time = datetime.datetime.today()
        Passenger.passenger_number += 1

    def call_elevator(self):
        #self.move(self)
        Elevator.passenger_call_elevator(self)
        pass


    def info(self):
        return 'pass no pass_num' + str(self.pass_num) + 'current_floor ' + str(self.current_floor) + 'required_floor ' + str(self.required_floor)

# https://www.ibm.com/developerworks/ru/library/l-python_part_9/index.html
###############################################################################################################
class PassThread(threading.Thread):
    def __init__(self, passenger):
        threading.Thread.__init__(self)
        self.daemon = True
        self.passenger = passenger
        self.setName(passenger.pass_num)
    def run(self):
        #while true:
        
        ###########################  тут про лифты ############################################

        #############################################################################################################################
        #                                                   код для нескольких лифтов
        #
        #nearest_elevator = get_nearest_elevator(passenger[Passenger.pass_num - 1] , elevator)
        #print("ближайший лифт ", nearest_elevator.elevator_number)
        #lift(passenger[Passenger.pass_num - 1] , nearest_elevator)

        #                                                   vyzov funckcii dlq odnogo lifta
        self.passenger.call_elevator()                                             
        #lift(passenger[Passenger.pass_num - 1])
        pass

    #https://compscicenter.ru/media/slides/python_2015_autumn/2015_12_07_python_2015_autumn_3KfewPJ.pdf
    def terminate(self):
        self._delete()

################################################################################################################
#                               Здесь создаем odnomomentno neskol;ko пассажиров
#
#def create_passengers(passenger):
#    # одновременно могут зайти несколько человек
#    random_num_of_pass = random.randint(1, 3)

#    print("Start random_num_of_pass = " , random_num_of_pass)
#    for i in range(random_num_of_pass):
#        required_floor = random.randint(1, 99)
#        current_floor = random.randint(1, 99)
#        while current_floor == required_floor: current_floor = random.randint(1, 99) # вызываемый этаж отличается от текущего  
#        # в список passengers добавляем новый объект Passenger
#        passenger.append(Passenger(current_floor , required_floor))

#        # каждый пассажир имеет одельный поток
#        p = PassThread(passenger[Passenger.pass_num - 1] , ele)
#        p.setName(Passenger.pass_num)
#        p.start()
#        print("Passenger num =" , p.getName())
#        print("PassThread name =" , p.getName())
#        log.write("PassThread name =" , p.getName())
#        print(psg[Passenger.pass_num - 1].info())
#########################################################################################################

#########################################################################################################
#                               zdes; sozdaem odnogo passa'ira
def create_passenger(passenger : Passenger):
    log.write('------------- новый пассажир ----------------')
    required_floor = random.randint(1, 99)
    current_floor = random.randint(1, 99)
    while current_floor == required_floor: current_floor = random.randint(1, 99) # вызываемый этаж отличается от текущего  
    # в список passengers добавляем новый объект Passenger
    psg = Passenger(current_floor , required_floor)

    # каждый пассажир это одельный поток
    p = PassThread(psg)
    passenger.append(p)
    p.start()
    psg.call_elevator()

    log.write("PassThread name = " + str(p.getName()))
    passinfo = str(psg.info())
    log.write("Passenger = " + str([passinfo]))





