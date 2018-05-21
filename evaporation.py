#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 21 06:14:43 2018
psychropy calculations author: remcmurry (https://github.com/remcmurry/Psychropy)
@author Scott
"""

import math

class evaporation(object):
    def __init__(self,A):
        self.ERate = 0
        self.Area = A
    
    def getSP(self,Tdb):   
        ''' Function to compute saturation vapor pressure in [kPa]
            ASHRAE Fundamentals handbood (2005) p 6.2, equation 5 and 6
                Tdb = Dry bulb temperature [degC]
                Valid from -100C to 200 C
        '''
        C1 = -5674.5359
        C2 = 6.3925247
        C3 = -0.009677843
        C4 = 0.00000062215701
        C5 = 2.0747825E-09
        C6 = -9.484024E-13
        C7 = 4.1635019
        C8 = -5800.2206
        C9 = 1.3914993
        C10 = -0.048640239
        C11 = 0.000041764768
        C12 = -0.000000014452093
        C13 = 6.5459673
     
        TK = Tdb + 273.15                     # Converts from degC to degK
        
        if TK <= 273.15:
            result = math.exp(C1/TK + C2 + C3*TK + C4*TK**2 + C5*TK**3 + 
                              C6*TK**4 + C7*math.log(TK)) / 1000
        else:
            result = math.exp(C8/TK + C9 + C10*TK + C11*TK**2 + C12*TK**3 + 
                              C13*math.log(TK)) / 1000
        return result
    
    def getHR(self, Tdb, RH, P=101.3):
        ''' Function to calculate humidity ratio [kg H2O/kg air]
            Given dry bulb and wet bulb temperature inputs [degC]
            ASHRAE Fundamentals handbood (2005)
                Tdb = Dry bulb temperature [degC]
                RH = Relative Humidity [Fraction or %]
                P = Ambient Pressure [kPa]
        '''
        Pws = self.getSP(Tdb)
        result = 0.62198*RH*Pws/(P - RH*Pws)    # Equation 22, 24, p6.8
        return result
    
    def getMaxSat(self,Tdb):
        c1 = 0.62198
        T = Tdb + 273.15 #Dry bulb temperature to kelvin
        Pws = math.e**(77.3450+0.0057*T-7235/T)/(T**8.2)
        maxSat = c1 *Pws /(101.3*1000-Pws)
        return maxSat
    
    def getERate(self,Tdb,RH,v,A): #kg of water / hour
        ec = 25 + 19 * float(v)
        self.Erate = ec * A * (self.getMaxSat(float(Tdb))-self.getHR(float(Tdb),float(RH))) 
        return int(self.Erate)


