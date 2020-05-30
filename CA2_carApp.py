# -*- coding: utf-8 -*-
"""
@author: DUDO3
"""

from car import ElectricCar, PetrolCar, DieselCar, HybridCar

import csv
import pandas as pd
import numpy as np

class CarRental(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = []

    def create_current_fleet(self):
        for i in range(6):
           self.electric_cars.append(ElectricCar())
        for i in range(20):
           self.petrol_cars.append(PetrolCar())
        for i in range(10):
           self.diesel_cars.append(DieselCar())
        for i in range(4):
           self.hybrid_cars.append(HybridCar())
        
# fleet of the rental company
    def dbs_fleet(self):
        print('Electric cars in stock ', 6)
        print('Petrol cars in stock ', 20 )
        print('Diesel cars in stock ', 10)
        print('Hybrid cars in stock ', 4)

# return available stock 
    def available_stock(self):
        print('Electric cars in stock ' + str(len(self.electric_cars)))
        print('Petrol cars in stock ' + str(len(self.petrol_cars)))
        print('Diesel cars in stock ' + str(len(self.diesel_cars)))
        print('Hybrid cars in stock ' + str(len(self.hybrid_cars)))

# function for car rent count
    def car_rent(self, available_stock, amount):
        if len(available_stock) < amount:
            print('Not enough cars in stock.')
            return
        total = 0
        while total < amount:
           available_stock.pop()
           total = total + 1

# function for car returns count
    def car_return(self, available_stock, ret_amount, dbs_fleet):
        if len(available_stock) + ret_amount > dbs_fleet:
            print('Too many cars for return or wrong type!!!')
            return
        total = 0
        while total < ret_amount:
           available_stock.append(ret_amount)
           total = total + 1

# processing car rentals and car returns
    def process_rental(self):
        answer = input('Would you like to rent (y) or return (n) a car?')
        if answer == 'y':
            answer = input('Please enter car type for hire (e) for Electric, (p) for Petrol, (d) for Diesel or (h) for Hybrid?')
            amount = int(input('How many cars would you like to rent?'))
            if answer == 'e':
                self.car_rent(self.electric_cars, amount)
            elif answer == 'p':
                self.car_rent(self.petrol_cars, amount)
            elif answer == 'd':
                self.car_rent(self.diesel_cars, amount)
            elif answer == 'h':
                self.car_rent(self.hybrid_cars, amount)
            else:
                return print('Incorrect type of car!!!')
        if answer == 'n':
            answer = input('Please enter type car type for return (e) for Electric, (p) for Petrol, (d) for Diesel or (h) for Hybrid? ')
            ret_amount = int(input('How many cars would you like to return? '))
            if answer == 'e':
                self.car_return(self.electric_cars, ret_amount, 6)
            elif answer == 'p':
                self.car_return(self.petrol_cars, ret_amount, 20)
            elif answer == 'd':
                self.car_return(self.diesel_cars, ret_amount, 10)
            elif answer == 'h':
                self.car_return(self.hybrid_cars, ret_amount, 4)
            else:
                return print('Incorrect type of car!!! ')

#create csv file with DBS fleet containing all cars for rental
    def dbs_fleet_csv(self):
        with open('dbs_fleet.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Car Type', 'DBS Fleet', 'Available stock', 'Rented stock'])
            writer.writerow(['Electric', 6, (str(len(self.electric_cars))),
                             6 - len(self.electric_cars)])
            writer.writerow(['Petrol', 20, (str(len(self.petrol_cars))),
                             20 - len(self.petrol_cars)])
            writer.writerow(['Diesel', 10, (str(len(self.diesel_cars))),
                             10 - len(self.diesel_cars)])
            writer.writerow(['Hybrid', 4, (str(len(self.hybrid_cars))),
                             4 - len(self.hybrid_cars)])

# return a summary of car rental status using pandas
    def summary(self):
        df = pd.DataFrame(data=pd.read_csv('dbs_fleet.csv'))
        print(df)

# main process
    def main(self):
        car_rental = CarRental()
        car_rental.create_current_fleet()
        proceed = 'y'
        while proceed == 'y':
            car_rental.process_rental()
            car_rental.dbs_fleet_csv()
            car_rental.summary()
            proceed = input('Would you like to continue (y/n)?')

car_rental = CarRental()
car_rental.main()







