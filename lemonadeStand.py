import random
import datetime

class LemonStand:
	def __init__(self,player_name):
		self.name = player_name
		self.temperature = random.randrange(40, 100)
        self.day = 0
        self.lemonade_selling_price = 0
        self.money = 1000
        self.number_sold = 0
        self.weather_add_on = random.choice("sunny","rainy","cloudy","blazing")


    def sell_lemons():
        while True:
            try:
                selling_price = int(raw_input('How much money will you charge for a cup of lemonade? (MAX $100,000) '))
                if selling_price in range(0, 100000):
                    break
                else:
                    print('Please enter a number')
                    continue
            except:
                print ('Please choose a number between 1 and 100.')
                continue

        
        supply_factor = float(100 - price) / 100  # 10% less demand for each ten cent price increase
        heat = 1 - (((100 - self.weather) * 2) / float(100))  # 20% less demand for each 10 degrees below 100
        num_cups = random.randrange(1, 200)
        if price == 0:
            self.lemonade = 0  # If you set price to zero, all your lemonade sells, for nothing.
            print('All of your lemonade sold for nothing because you set the price to zero.')
            self.day += 1
            self.weather = random.randrange(50, 100)
            self.lemonade_price = random.randrange(1, 10)
        demand = int(round(cups * price_factor * heat_factor))
        if demand > self.lemonade:
            print(
                'You only have ' + str(self.lemonade) + ' cups of lemonade, but there was demand for ' + str(
                    demand) + '.')
            demand = self.lemonade
        revenue = demand * round((float(price) / 100), 2)
        self.lemonade -= demand
        self.money += revenue
        self.day += 1
        self.weather = random.randrange(50, 100)
        self.lemonade_price = random.randrange(1, 10)
        print('You sold ' + str(demand) + ' cup(s) of lemonade and earned $' + str(revenue) + ' dollars!\n')





























