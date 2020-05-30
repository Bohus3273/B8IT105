# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 07:08:44 2020

@author: DUDO3
"""

class Car(object):
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour
    
    def getMake(self):
        return self.__make
    
    def getMileage(self):
        return self.__mileage
    
    def setColour(self, value):
        self.__colour = value
    
    def setMake(self, value):
        self.__make = value
    
    def setMileage(self, value):
        self.__mileage = value
        
    def move(self, distance):
        print('Car has moved', distance, 'kilometres')
        self.__mileage += distance

    def paint(self, colour):
        print('Car has been painted', colour)
        self.__colour = colour

class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 0
        
    def getNumberFuelCells(self):
        return self.__numberFuelCells
    
    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__transmission = ''
        
    def getTransmission(self):
        return self.__transmission
    
    def setTransmission(self, value):
        self.__transmission = value

class DieselCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__transmission = ''
        
    def getTransmission(self):
        return self.__transmission
    
    def setTransmission(self, value):
        self.__transmission = value
        
class HybridCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__transmission = ''
        
    def getTransmission(self):
        return self.__transmission
    
    def setTransmission(self, value):
        self.__transmission = value


    
    
    
    
    
    