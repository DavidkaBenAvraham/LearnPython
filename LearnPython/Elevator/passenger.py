import random
from elevator import *
import logic
import datetime
import time
import threading


passenger = [] # list of passengers '''


class Passenger:
    pass_num = 0
    required_floor = 0 
    current_floor = 0
    floor_group = 0 # 0: 1 - 33; 2 - 34-66; 3 - 67-99
    direction = 0 #0 - stopped; "1" - up; "-1" - down
    #time = today.strftime("%Y-%m-%d %H:%M:%S")
    time = datetime.datetime.today()
    
    def __init__(self , current_floor = 0, required_floor = 0):
        """
        Зашел новый зашел человек в здание
        """
        Passenger.pass_num += 1
        self.pass_num = Passenger.pass_num
        self.current_floor = current_floor
        self.required_floor = required_floor
        
        if(required_floor > 1 and required_floor < 34):
            self.floor_group = 1
        elif(required_floor > 34 and required_floor < 67):
            self.floor_group = 2
        else:
            self.floor_group = 3

        self.direction = 1 if current_floor < required_floor else -1
        self.time = datetime.datetime.today()
    def info(self):
        return ["пассажир {} едет с {} этажа на {} этаж. Направление {}  время {}" .format(self.pass_num ,  self.current_floor , self.required_floor , self.direction  ,  self.time.strftime(" %H:%M:%S"))]

class PassThread(threading.Thread):
    def __init__(self,passenger):
        threading.Thread.__init__(self)
        self.daemon = True
        self.passenger = passenger
        self.setName(Passenger.pass_num - 1)
    def run(self):
        #while true:
        
        ###########################  тут про лифты ############################################

        #############################################################################################################################
        #                                                   код для нескольких лифтов
        #
        #nearest_elevator = get_nearest_elevator(passenger[Passenger.pass_num - 1] , elevator)
        #print("ближайший лифт ", nearest_elevator.elevator_number)
        #lift(passenger[Passenger.pass_num - 1] , nearest_elevator)

        lift(passenger[Passenger.pass_num - 1] , elevator[0])
        pass

#Здесь создаем входящих в здание пассажиров

def start_passengers(passenger):
    # одновременно могут зайти несколько человек
    random_num_of_pass = random.randint(1, 3)
    print("Start random_num_of_pass = " , random_num_of_pass)
    for i in range(random_num_of_pass):
        required_floor = random.randint(1, 99)
        current_floor = random.randint(1, 99)
        while current_floor == required_floor: current_floor = random.randint(1, 99) # вызываемый этаж отличается от текущего       
        passenger.append(Passenger(current_floor , required_floor))

        # каждый пассажир имеет одельный поток
        p = PassThread(passenger)
        p.setName(Passenger.pass_num)
        p.start()
        print("PassThread name =" , p.getName())
        log.write("PassThread name =" , p.getName())

        print(passenger[Passenger.pass_num - 1].info())




