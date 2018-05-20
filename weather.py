# -*- coding: utf-8 -*-
"""
Weather API handler using Yahoo Weather API and API wrapper (Open Weather Map)
Created on Sat May 19 19:26:40 2018

@author: Scott
"""
from weather import Weather, Unit

class locationWeather(object):
    def __init__(self, location):
        self.weather = Weather(unit=Unit.CELSIUS).lookup_by_location(location)
        self.condition = self.weather.condition
    
    def getForecasts(self):
        return self.weather.forecast #returns 5 day forecast objects
    
    def getWeather(self):
        return self.weather #returns weather object
    
    