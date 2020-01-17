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
                return stop_list[i]
        return "Not a valid position"

    def get_departure_time(self):
        pass
