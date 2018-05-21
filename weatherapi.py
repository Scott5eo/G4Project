# -*- coding: utf-8 -*-
"""
Weather API handler using Yahoo Weather API and API wrapper (Open Weather Map)
Created on Sat May 19 19:26:40 2018
@author: Scott
"""
from weather import Weather, Unit

class locationWeather(object): #This is a weather-api class that uses Weather-api, a yahoo weather api wrapper.
    def __init__(self, location): #this loads the initial weather of the location given
        self.location = location
        self.weather = Weather(unit=Unit.CELSIUS).lookup_by_location(self.location)
        self.condition = self.weather.condition
    
    def getForecasts(self):
        return self.weather.forecast #this returns 5 day forecast objects which to be used later
    
    def getWeather(self):
        return self.weather #returns weather object which contains the day's weather
    
    def getWind(self):
        return self.weather.wind.speed #Returns wind speed
    
    def getForecastHighs(self):
        dateHighs = {}
        for forecast in self.getForecasts():
            dateHighs[forecast.date] = forecast.high
        return dateHighs #returns a dictionary of highs to keys of days
    
    def getForecastDates(self):
        dates = []
        for forecast in self.getForecasts():
            dates.append(forecast.date)
        return dates #return a list of days in order of forecast to be used with evaporation estimation in another class.
    
