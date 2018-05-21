#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main class
Created on Mon May 21 19:39:34 2018


@author: Scott
"""
from locationWeather import locationWeather
from evaporation import evaporation
import tkinter

class client(object):
    def __init__(self, location, surface_area):
        self.location = location
        self.weather = locationWeather(self.location)
        self.evaporation = evaporation(surface_area)
        self.root = tkinter.Tk()
        
    def run(self):
        wind = 0.277778* self.weather.getWind()
        temp = self.weather.getTemperature()
        RH = float(self.weather.getHumidity()) * 0.01
        eRate = self.evaporation.getERate(temp,RH,wind,self.evaporation.Area)
        current_eRate = "The current evaporation rate with " + str(temp) + " degree celsius, " + str(RH) + " humidity, and " + str(wind) + " wind speed, the current evaporation rate is " + str(int(eRate)) + "kg/hour. \n" 
        next10days = ""
        estimate = 0.0
        for day in self.weather.getForecastDates():
            next10days += str(self.weather.getForecastHighs()[day]) + ", "
            estimate += self.evaporation.getERate(int(self.weather.getForecastHighs()[day]),0.5,5.5,self.evaporation.Area) * 8
        estimate_msg = "The estimation of water evaporated over next 10 days with daily highs of " + str(next10days) + "is " + str(estimate) +"kg."
        for i in range(10):
            print()
        print(current_eRate)
        print(estimate_msg)
dubai = client('dubai',32000)
dubai.run()