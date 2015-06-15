import random
import datetime

"""
This was my initial class attempt - doesn't do anything right now
"""
class Ingredients:
    def __init__(self,name,amount,cost):
        self.name = name
        self.amount = amount
        self.cost = cost

    def get_amount(self):
        return self.amount

    def increase_amount(self,amount):
        self.amount += amount

    def decrease_amount(self,amount):
        self.amount -= amount

    def get_cost(self):
        return self.cost



class LemonStand:
    def __init__(self,player_name):
        self.name = player_name
        self.temperature = random.randrange(40, 100)
        self.day = 0
        self.lemonade_selling_price = 0
        self.money = 1000
        self.number_sold = 0
        self.weather_add_on = random.choice(["sunny","rainy","cloudy"])
        self.cups_available = 0
        self.lemonade_cost = .50

    def display_stats(self):
        """ Display all data for the lemonade stand."""

        if self.day == 0:
            print('\nHello ' + self.name + '!\n')
        print('Day: ' + str(self.day))
        print('Weather: ' + "Temp: " + str(self.temperature) + "    Forecast: " + self.weather_add_on)
        print('Money: ${:,.2f}'.format(self.money))
        print('Cups Available: ' + str(self.cups_available))
        print('Cost to make Lemonade: ${:,.2f}'.format(self.lemonade_cost))
        print('============================' + '\n')

    def buy_lemonade(self):
        while True:
            try:
                quantity = int(raw_input('How much ingredients would you like to buy? (in cups of lemonade)'))
                money_check = self.money - quantity*.50
                print money_check
                if money_check > 0:
                    self.money = self.money - quantity*.50
                    self.cups_available += quantity
                    break
                else:
                    print('You do not have enough money. Please re-enter amount.')
                    continue
            except:
                print ('Value entered is not a number. How much ingredients would you like? (in cups of lemonade)')
                continue

    def sell_lemonade(self):
        while True:
            try:
                selling_price = int(raw_input('How much money will you charge for a cup of lemonade? (MAX $100) '))
                if selling_price in range(0, 100):
                    break
                else:
                    print('Please enter a number between 0 and $100')
                    continue
            except:
                print ('Please enter a number between 0 and $100')
                continue
        if selling_price < 4:
            max_number_sold = 500
        elif selling_price < 8:
            prob_max_sold_chance = float(random.randrange(4,11))
            prob_max_sold = float(prob_max_sold_chance/10.0)
            max_number_sold = round((250*prob_max_sold),0)
            print max_number_sold
        elif selling_price < 12:
            prob_max_sold_chance = float(random.randrange(0,4))
            prob_max_sold = float(prob_max_sold_chance/10.0)
            max_number_sold = round((100 * prob_max_sold),0)
        else:
            prob_max_sold_chance = float(random.randrange(0,100))
            prob_max_sold = float(prob_max_sold_chance/1000)
            max_number_sold = round((5 * prob_max_sold),0)
        if self.weather_add_on == "sunny":
            max_number_sold = round((max_number_sold * 1.5),0)
        elif self.weather_add_on == "rainy":
            max_number_sold = round((max_number_sold * .75),0)
        temp_adder = float((self.temperature - 70) / 100.0)
        temp_multiplier = 1 + temp_adder
        max_number_sold = round((temp_multiplier * max_number_sold),0)
        print max_number_sold
        if max_number_sold == 0 or max_number_sold == 1:
            final_demand_cups = 0
        else:
            if max_number_sold == 77 or max_number_sold == 777:
                print "YOU HIT THE JACKPOT!"
                self.cups_available += 100000
            final_demand_cups = random.randrange(0, max_number_sold)
            print "Good Chance",final_demand_cups
        if self.cups_available - final_demand_cups >= 0:
            self.cups_available = self.cups_available - final_demand_cups
            money_made_day = round(final_demand_cups*selling_price,2)
            print "Money Made Today: ${:,.2f}".format(money_made_day)
            self.money += money_made_day
            string_money = "$"+str(money_made_day)
            print "You have sold " + str(final_demand_cups) + " cups and made ${:,.2f}".format(money_made_day)
            print('============================' + '\n')
            self.day += 1
            self.money -= 25
            self.weather_add_on = random.choice(["sunny","rainy","cloudy"])
            self.temperature = random.randrange(40, 100)
            self.lemonade_cost = random.choice([.10,.25,.50,.75,1,1.5,2])

        else:
            money_made_day = round(self.cups_available*selling_price,2)
            self.money += money_made_day
            print "You ran out of cups!"
            print "You would have sold " + str(final_demand_cups) + " cups but instead sold " + str(self.cups_available) + " and made ${:,.2f}".format(money_made_day)
            print('============================' + '\n')
            self.day += 1
            self.cups_available = 0
        self.money -= 25
        self.weather_add_on = random.choice(["sunny","rainy","cloudy"])
        self.temperature = random.randrange(40, 100)
        self.lemonade_cost = random.choice([.10,.25,.50,.75,1,1.5,2])


def check_day():
    daylight = {1:[7,16],2:[7,17],3:[7,18],4:[7,19],5:[6,20],6:[5,20],7:[5,20],8:[6,20],9:[6,19],10:[7,18],11:[6,17],12:[7,16]}
    current_time = datetime.datetime.now()
    month_of_day = current_time.month
    time_of_day = current_time.hour
    day_evaluating = daylight[month_of_day]
    if time_of_day in range(day_evaluating[0],day_evaluating[1]+1):
        return True
    else:
        return False

def main():

    """ Create new Lemonade object and play game, or exit.
    """
    choice = ''
    while choice not in ['y', 'n']:
        choice = raw_input('Open a new stand? (y/n) ')
        if choice == 'y':
            name = raw_input('What is your name? ')
            stand = LemonStand(name)
            stand.display_stats()
            while True:
                choice = raw_input('Enter 1 to buy lemonade. Enter 2 to sell lemonade. 3 to quit. ')
                if choice == '1':
                    stand.buy_lemonade()
                    stand.display_stats()
                    continue
                elif choice == '2':
                    stand.sell_lemonade()
                    stand.display_stats()
                    continue
                elif choice == '3':
                    print('Goodbye!')
                    return
                else:
                    print('You must choose either 1 or 2 or 3.')
                    continue
        elif choice == 'n':
            print('Goodbye!')
            return

is_it_dark = check_day()
if is_it_dark:
    main()
else:
    print ("It's dark outside, you can't sell lemonade")

