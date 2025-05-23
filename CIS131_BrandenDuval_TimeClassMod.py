'''
script: Modifying the Internal Data Representation of a Class
action: modifies Class "Time" to store the time as the total seconds since midnight
author: Branden Duval
date: 03/04/2025
'''

class Time:
    '''Class Time with read-write properties.'''

    def __init__(self, hour=0, minute=0, second=0):
        '''Initialize each attribute.'''
        hour *= 3600 # 0-23 * 3600 takes the hour input from the constructor and converts it to seconds
        minute *= 60 # 0-59 * 60 takes the minute input from the constructor and converts it to seconds 
        second # 0-59
        self._total_seconds = hour + minute + second # adds all the previous values into one variable 

    @property
    def hour(self):
        '''Return the hour'''
        return self._total_seconds // 3600 # floor divides the total seconds by the seconds in an hour 

    @hour.setter
    def hour(self, hour):
        '''Set the hour.'''
        
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        
        hour *= 3600 # see line 9
        self._total_seconds = hour + self.minute + self.second # adds the values back into the total seconds variable

    @property
    def minute(self):
        '''Rerturn the minute.'''
        return self._total_seconds % 3600 // 60 # uses modulus to discern an hour and then floor divides to find the minute value

    @minute.setter
    def minute(self, minute):
        '''Set the minute.'''
        
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        
        hour = self.hour * 3600 # sets hour to be self.hour attribute converted to seconds
        minute *= 60 # see line 10
        self._total_seconds = hour + minute + self.second # adds the values back into the total seconds variable

    @property
    def second(self):
        '''Return the second.'''
        return self._total_seconds % 60 # uses modulus to calculate the seconds value

    @second.setter
    def second(self, second):
        '''Set the second.'''
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')
        
        hour = self.hour * 3600 # sets hour to be self.hour attribute converted to seconds
        minute = self.minute * 60 # sets minute to be self.minute attribute converted to seconds
        self._total_seconds = hour + minute + second # adds the value back into the total seconds variable

    def set_time(self, hour=0, minute=0, second=0):
        '''Set values of hour, minute, and second.'''
        
        hour *= 3600 # see line 9
        minute *= 60 # see line 10
        self._total_seconds = hour + minute + second # adds the variables back into the total seconds variable

    def __repr__(self):
        '''Return Time string for repr().'''
        return (f'Time (hour={self.hour}, minute={self.minute}, ' +
                f'second={self.second})')

    def __str__(self):
        '''Print Time in 12-hour clock format.'''
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}'+
                (' AM' if self.hour < 12 else ' PM'))

'''debug nonesense'''    
# a_time = Time(1, 0, 0)
# a_time.hour = 10
# a_time.minute = 10
# a_time.second = 10
# print(a_time.hour)
# print(a_time.minute)
# print(a_time.second)