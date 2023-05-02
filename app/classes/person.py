import datetime
from utils.logger import logger

class Person:
    def __init__(self, name, age, weight, height, birthday):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.birthday = birthday
    
    def eat(self, food):
        if food == 'steak':
            self.weight += 1.0
            logger.info(f"{self.name} ate steak; gimme da gains (1lb)! {self.name} now weighs {self.weight} lbs.")
        elif food == 'salad':
            # eating salad doesn't affect weight
            logger.info(f"{self.name} ate salad; so healthy! {self.name} still weighs {self.weight} lbs.")
        else:
            logger.info(f"Error: Unknown food '{food}'")
    
    def run(self, miles):
        if miles > 0:
            self.weight = round(self.weight - 0.1 * miles, 1) 
            logger.info(f"{self.name} ran {miles} miles; let's get it! {self.name} lost {round(0.1*miles, 1)} lbs and now weighs {self.weight} lbs.")
        else:
            logger.info(f"{self.name} took a well deserved rest day.")
    def _age(self):
        self.age += 1
        logger.info(f"Happy {self.age} birthday {self.name}! Time flies innit?!")
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, weight={self.weight}, height={self.height}, birthday={self.birthday})"

