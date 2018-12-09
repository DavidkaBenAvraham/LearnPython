import random
from elevator import Elevator
import datetime


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
        return ["пассажир {} едет с {} этажа на {} этаж. Направление {}  время {}" .format(self.pass_num , self.current_floor , self.required_floor , self.direction  ,  self.time.strftime(" %H:%M:%S"))]

#Здесь создаем входящих 
def passenger_entrance(passenger):
    required_floor = random.randint(1, 99)
    current_floor = random.randint(1, 99)
    while current_floor == required_floor: current_floor = random.randint(1, 99) # вызываемый этаж отличается от текущего       
    passenger.append(Passenger(current_floor , required_floor))

# создаем пассажиров
def get_passengers():
        # люди заходят не всегда, а с некоторым интервалом
    time.sleep(random.randint(1, 5)) # от одной до пяти секунд
    passenger_entrance(passenger)
    print(passenger[Passenger.pass_num - 1].info())
    nearest_elevator = get_nearest_elevator(passenger[Passenger.pass_num - 1] , elevator)
    print("ближайший лифт ", nearest_elevator.elevator_number)
    lift(passenger[Passenger.pass_num - 1] , nearest_elevator)


# какая то ненужная хуйня
def get_passengers_by_group_elevators(group , passenger):
    p_out = []
    for p in passenger:
        if(p.floor_group == group):
            p_out.append(p)
    return p_out
