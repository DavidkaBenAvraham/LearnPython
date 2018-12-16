import random
import time
import threading
import logic
import passengers

#Passenger = passengers.Passenger()
if __name__ == "__main__":
    pass

class Elevator:
    """
    """
    floor_group = 0 # 0: 1 - 33; 2 - 34-66; 3 - 67-99
    current_floor = 0
    people_lifted = 0
    elevator_direction = 0 #0 - stopped; "1" - up; "-1" - down
    maintenance_date = ""
    elevator_number = 0
    max_num_of_people_in_elevator = 10
    #Сколько людей находится в лифте
    people_lifted = 0
    passengers_in_elevator = []
    remember_called_passengers = [] # запоминаем вызвавших лифт
 
    # Конструктор класса. Вызывается при создании экземпляра класса
    def __init__(self,floor_group = 0):
        self.floor_group = floor_group
        Elevator.floor_group = floor_group

        self.current_floor = random.randint(1,99)
        Elevator.current_floor = self.current_floor

        self.elevator_direction = 0
        Elevator.elevator_direction = self.elevator_direction

        Elevator.elevator_number = 1
        self.elevator_number = Elevator.elevator_number

        # переменная экземпляра класса. Количество людей перевезенных КОНКРЕТНЫМ лифтом
        self.people_lifted = 0
        Elevator.people_lifted = self.people_lifted

    def lift(self, passenger : Passenger):
        # print("пассажир на {} этаже, лифт на {} этаже" .format(passenger.current_floor , self.current_floor))
        log_str = str('пассажир на '+ str(passenger.current_floor) +' этаже, лифт на  '+ str(self.current_floor) +' этаже   Поехали!  ')
        log.write(log_str)
        print(log_str)
        #Лифт стоит на месте
        if elevator.elevator_direction == 0:
            if passenger.current_floor < self.current_floor:
                self.elevator_direction = 1
                log.write("вверх ")
            else:
                self.elevator_direction = -1
                log.write("вниз ")
        #else:
        #    self.elevator_direction = 0
        #    log.write("на этаже")
        self.remember_called_passengers.append(passenger)
        self.elevator_move(passenger)

    def passenger_call_elevator(passenger: Passenger):
        log_str = str('пассажир на '+ str(passenger.current_floor) +' этаже, лифт на  '+ str(self.current_floor) +' этаже   Поехали!  ')
        log.write(log_str)
        #Лифт стоит на месте
        if Elevator.elevator_direction == 0:
            if passenger.current_floor < Elevator.current_floor:
                Elevator.elevator_direction = 1
                log.write("вверх ")
            else:
                Elevator.elevator_direction = -1
                log.write("вниз ")
        #else:
        #    self.elevator_direction = 0
        #    log.write("на этаже")
        Elevator.remember_called_passengers.append(passenger)
        Elevator.elevator_move(passenger)
        pass
    

    def elevator_move(self, passenger : Passenger):
        #while self.current_floor != passenger.current_floor:
        #    #print("лифт на {} этаже " .format(self.current_floor), end='\r')
        #    log_str = 'elevator on '+ str(self.current_floor) + ' \t passenger no '+ str(passenger.pass_num) +' \t on ' + str(passenger.current_floor)
        #    log.write(log_str)
        #    print(log_str)
        #    time.sleep(0.5)
        #    if self.elevator_direction == 1:
        #        self.current_floor -=1
        #    else:
        #        self.current_floor +=1
        #print("Лифт {} подан! пассажир на {} этаже, лифт на этаже {}" .format(self.elevator_number , passenger.current_floor , self.current_floor))
        #log.write("Elevator served! ")
        
        if self.elevator_direction == 1:
                self.current_floor -=1
        else:
                self.current_floor +=1

        time.sleep(2)
        #sa'aem passa'ira v lift

        for psg in self.remember_called_passengers:
            if psg.current_floor == self.self.current_floor:
                self.passengers_in_elevator.append(passenger)
                log.write('passenger ' + passenger.pass_num +'in elevator ')
                print(' passenger '+ + passenger.pass_num + 'in elevator ')
                print("---------------------------------------")
                self.remember_called_passengers.remove(psg) 

       
    # Метод печатающий информацию о конкретном лифте
    def info(self):
        return [self]
        pass

#class ElevatorThread(threading.Thread):
#    def __init__(self,elevator):
#        threading.Thread.__init__(self)
#        self.daemon = True
#        self.passenger = passenger
#        self.elevator = elevator
#    def run(self):
#        while True:
#            # люди заходят не всегда, а с некоторым интервалом
#            time.sleep(random.randint(1, 5)) # от одной до пяти секунд
#            start_passengers(passenger)

# ------------------------------------------------------------------------------------------------
#                                           создаем лифт
#код для нескольких
#def create_elevators(elevator , num_of_elevators):
#    for i in range(num_of_elevators):
#        elevator.append(Elevator())





#############################################################################################################################
#                                                   код для нескольких лифтов
#
# находим ближайший лифт
# 
#def get_nearest_elevator(passenger , elevator):
#    nearest_elevator = []
#    for e in range(len(elevator)):
#        #проверяем направление движения лифта
#        if elevator[e].elevator_direction == passenger.direction or elevator[e].elevator_direction == 0:
#            #вычиляем модуль разности этажей
#            delta = abs(passenger.current_floor - elevator[e].current_floor)
#            nearest_elevator.append([delta , elevator[e].elevator_number , elevator[e].elevator_direction])
#    #сортируем по дельта
#    nearest_elevator.sort()
#    #возвращаем первый отсортированный (минимальная дельта)
#    return elevator[nearest_elevator[0][1]-1]
#def lift(passenger , elevator):
#    print("пассажир на {} этаже, лифт на {} этаже" .format(passenger.current_floor , elevator.current_floor))
#    log.write("пассажир на {} этаже, лифт на {} этаже" .format(passenger.current_floor , elevator.current_floor))
#    print("поехали")
#    #if elevator.elevator_direction == 0:
#    if passenger.current_floor < elevator.current_floor:
#        elevator.elevator_direction = 1
#        print("вверх" , elevator.elevator_direction)
#    elif passenger.current_floor > elevator.current_floor:
#        elevator.elevator_direction = -1
#        print("вниз" , elevator.elevator_direction)
#    else:
#        print("на этаже")
#    elevator_move(passenger , elevator)
##########################################################################################################################################

