# -*- coding: utf-8 -*-
"""
Weather API handler using Yahoo Weather API and API wrapper
API handling code done by Ushir, editted by Scott
@author: Ushir, Scott
"""
from weather import Weather, Unit

class locationWeather(object):
    def __init__(self, location):
        self.location = location
        self.weather = Weather(unit=Unit.CELSIUS).lookup_by_location(self.location)
        self.condition = self.weather.condition
    
    def getForecasts(self):
        return self.weather.forecast #returns 5 day forecast objects
    
    def updateWeather(self):
        self.weather = Weather(unit=Unit.CELSIUS).lookup_by_location(self.location)
        self.condition = self.weather.condition
    
    def getWind(self):
        return float(self.weather.wind.speed)
    
    def getForecastHighs(self):
        dateHighs = {}
        for forecast in self.getForecasts():
            dateHighs[forecast.date] = forecast.high
        return dateHighs #returns a dictionary
    
    def getTemperature(self):
        return float(self.condition.temp)
    
    def getForecastDates(self):
        dates = []
        for forecast in self.getForecasts():
            dates.append(forecast.date)
        return dates #return a list 
    
    def getHumidity(self):
        self.updateWeather()
        return float(self.weather.atmosphere['humidity'])
