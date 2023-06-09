import datetime
import time
import random
import os
import sys
import numpy as np
from classes.person import Person
from utils.logger import logger

VALID_FOODS = ['steak', 'salad']
SLEEP_SECS = int(os.getenv('SLEEP_SECS'))

def main():
    current_date = datetime.date.today()
    # Create Person object
    birthday = datetime.date(1987, 5, 14)
    p = Person(name='John', age=35, weight=190.0, height=70.0, birthday=birthday)
    logger.info(f"Hello {p.name}! Ready to live life? Let's go!")
    # Life loop
    while True:
        logger.info(f"Good morning! Today is {current_date}")
        # If birthday, age 1 year
        if (current_date.month == birthday.month) \
            and (current_date.day == birthday.day):
            p.age()
        # Run
        distance = int(np.random.normal(5, 10))
        p.run(distance)
        # Eat
        food = random.choice(VALID_FOODS)
        p.eat(food)
        # Sleep 10 seconds (1 day)
        logger.info(f"What a day! Time for sleep.")
        logger.info(f"Sleeping {SLEEP_SECS} seconds...")
        current_date += datetime.timedelta(days=1)
        time.sleep(SLEEP_SECS)
    
if __name__ == "__main__":
    main()
