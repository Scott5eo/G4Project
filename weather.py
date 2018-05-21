# -*- coding: utf-8 -*-
"""
Weather API handler using Yahoo Weather API and API wrapper (Open Weather Map)

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
    
    def getForecastHighs(self):
        dateHighs = {}
        for forecast in self.getForecasts():
            dateHighs[forecast.date()] = forecast.high()
        return dateHighs #returns a dictionary
    
    def getForecastDates(self):
        dates = []
        for forecast in self.getForecasts():
            dates.append(forecast.date())
        return dates #return a list 
