import numpy as np
import scipy
from matplotlib import pyplot
from scipy.integrate import odeint

train_types = ['bullet', 'limited', 'local', 'limited']
departures = [9, 10, 10.5, 10.75]

class CalTrain:
    def __init__(self, train_types, departures):
        self.num_trains = len(train_types)
        self.time = 0
        self.trains = []
        #Create trains in system
        for n in range(len(train_types)):
            self.trains.append(Train(train_types[n-1], departures[n-1]));

    def calculate_arrival_times(self):
        arrivals = []
        for t in self.trains:
            arrivals.append(t.calculate_arrival_time())
        print(arrivals)

    def get_train_positions(self):
        positions = []
        for t in self.trains: positions.append(t.position)
        return positions

    def get_train_speeds(self):
        speeds = []
        for t in self.trains: speeds.append(t.speed)
        return speeds

    def get_train_accelerations(self):
        accels = []
        for t in self.trains: accels.append(t.acceleration)
        return accels

    def get_limit_position(self, train):
        position = train.position
        positions = self.get_train_positions()
        for i in range(len(positions)):
            if positions[i] == position:
                continue
            elif positions[i] > position:
                next_train_index = positions[i]
                next_train = trains[i]
        next_train = 10
        next_stop = train.get_next_stop()
        if next_stop < next_train:
            print("Next limiting object is a stop", next_stop)
            return next_stop
        else:
            print("Next limiting object is a train", next_train)
            return next_train

    def all_trains_travel(self):
        for t in self.trains:
            limit_position = self.get_limit_position(t)
            t.travel(limit_position)

class Train:
    def __init__(self, train_type, departure):
        self.train_type = train_type
        self.departure = departure
        self.position = 0
        self.speed = 0
        self.acceleration = 0
        self.speed_limit = 2
        self.accel_limit = 1
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
                return stop_list[i]
        return "Not a valid position"

    def calculate_arrival_time(self):
        print("Train has departed")

    def travel(self, limit_position):
        time_step = 0.1
        stop_distance = limit_position - self.position
        stop_limit = np.sqrt(2*self.accel_limit*stop_distance)
        if (stop_limit > self.speed_limit) and (self.speed < self.speed_limit+self.acceleration * time_step):
            #accelerate
            self.acceleration = self.accel_limit
            self.speed +=  self.acceleration * time_step
            self.position += self.speed * time_step
        elif stop_limit < self.speed_limit:
            #decelerate
            self.acceleration = -self.accel_limit
            self.speed +=  self.acceleration * time_step
            self.position += self.speed * time_step
        else:
            #maintain constant velocity
            self.position += self.speed * time_step

c = CalTrain(train_types, departures)
c.all_trains_travel()
c.get_train_positions()
c.get_train_speeds()
c.get_train_accelerations()
