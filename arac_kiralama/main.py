# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 01:13:45 2024

@author: emirh
"""

class Vehicle_rent(object): #parent
    def __init__(self, stock):
        self.stock = stock
        self.now = 0
    
    def display_stock(self):
        if self.stock < 1:
            print(f"{self.stock} vehicle available to rent")
            
        else:
            print(f"{self.stock} vehicle available to rent")
        
        return self.stock
        
    def rent_hourly(self, n):
        
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print(f"Sorry we have only {self.stock} vehicle")
            return None
        else:
            return self.stock


    def rent_daily(self, n):
        #rent daily
        pass
    
    def return_vehicle(self, request, brand):
        # iade , para ödeme
        pass
    
    
    
class Car_rent(Vehicle_rent): #child class
    def __init__(self):
        pass
    
    def discount():
        pass

class Bike_rent(Vehicle_rent):# child class

    def __init__(self):
        pass






class Customer:
    def __init__(self):
        pass
    
    def request_vehicle():
        pass
    
    def return_vehicle():
        pass