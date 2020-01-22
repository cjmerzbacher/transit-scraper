import pandas as pd

class Trip:
    def __init__ (self, id, train_type, timepoints):
        self.id = id
        self.train_type = train_type
        self.timepoints = pd.DataFrame(timepoints, columns = ['timestamp', 'latitude', 'longitude'])
    def add_timepoint(self, timestamp, latitude, longitude):
        self.timepoints = self.timepoints.append({'timestamp':timestamp, 'latitude':latitude, 'longitude':longitude}, ignore_index=True)
