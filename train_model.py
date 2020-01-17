import numpy as np
import scipy
from matplotlib import pyplot
from scipy.integrate import odeint

train_types = ['b', 'l', 's', 'l']
departures = [9, 10, 10.5, 10.75]

class CalTrain:
    def __init__(self, train_types, departures):
        self.num_trains = len(train_types)
        self.train_types = train_types
        self.departures = departures
        self.arrivals = self.calculate_arrival_times(train_types, departures)
    def calculate_arrival_times(self, train_types, departures):
        arrivals = []
        for i in range(len(train_types)):
            if train_types[i] == 'b':
                arrivals.append(departures[i]+10)
            elif train_types[i] == 'l':
                arrivals.append(departures[i]+15)
            elif train_types[i] == 's':
                arrivals.append(departures[i]+20)
            else:
                print('Not a valid train type!')
        print(arrivals)

class Train:
    def __init__(self, train_type, arrival):
        self.train_type = train_type
        self.arrival = arrival
        self.position = 0
        self.speed = 0
<<<<<<< HEAD
        self.acceleration = 1
        self.speed_limit = 2
        #Select the stop list based on train type
        if self.train_type ==  'bullet': self.stop_list = [0, 4, 8, 10]
        elif self.train_type ==  'limited': self.stop_list = [0, 2, 4, 5, 8, 10]
        elif self.train_type ==  'local': self.stop_list = [0, 1, 2, 4, 5, 6, 8, 10]
        else: raise ValueError('Not a valid train type.')

    def get_next_stop(self):
        stop_list = self.stop_list
        for i in range(len(stop_list)):
            if self.position == stop_list[i]:
                #print("At stop", self.position)
                return self.position
            elif self.position < stop_list[i]:
                #print("Next stop", stop_list[i])
=======

        #Select the stop list based on train type
        switch (self.train_type){
        case 'bullet': self.stop_list = [0, 4, 8, 10]
            break;
        case 'limited': self.stop_list = [0, 2, 4, 5, 8, 10]
            break;
        case 'local': self.stop_list = [0, 1, 2, 4, 5, 6, 8, 10]
            break;
        }

    def get_next_stop(self):
        for i in range(len(stop_list)):
            if self.position == stop_list[i]:
                print("At stop", self.position)
                return self.position
            elif self.position < stop_list[i]:
                print("Next stop", stop_list[i])
>>>>>>> 5c00a3303bf99a764c4d2015646786c4372b4955
                return stop_list[i]
        return "Not a valid position"

    def get_departure_time(self):
<<<<<<< HEAD
        print("Train has departed")

    def travel(self, limit_position):
        time_step = 0.1
        stop_distance = limit_position - self.position
        stop_limit = np.sqrt(2*self.acceleration*stop_distance)
        if (stop_limit > self.speed_limit) and (self.speed < self.speed_limit+self.acceleration * time_step):
            #accelerate
            self.speed +=  self.acceleration * time_step
            self.position += self.speed * time_step
        elif stop_limit < self.speed_limit:
            #decelerate
            self.speed -=  self.acceleration * time_step
            self.position += self.speed * time_step
        else:
            #maintain constant velocity
            self.position += self.speed * time_step



t = Train('local', 10.25)
=======
        pass
>>>>>>> 5c00a3303bf99a764c4d2015646786c4372b4955
