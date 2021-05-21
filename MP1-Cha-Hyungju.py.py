import random
import math


nook_inventory = {}
redd_inventory = {}

'''
# 1 Enter items into your inventory system
temp_inventory = []
while True:
    item = input('Add an item to the inventory list: ')
    if item == 'stop':
        print('\n--- Nook Inventory ---')
        for i in temp_inventory:
            print(i)
        break
    temp_inventory.append(item)


# 2 Set a price for your items, and run some computations
print('\n')
for item in temp_inventory:
    price = input('[' + item + '] Enter price: ')
    nook_inventory[item] = int(price)
'''
#######################
nook = {'apple': 10, 'orange': 23, 'melon': 32, 'amond': 7, 'peanut': 3, 'carrot': 4, 'meat': 19}
nook_inventory = nook
#########################

low_price = 1000000
high_price = 0
avg_price = 0

for price in nook_inventory.values():
    if price < low_price:
        low_price = price

    if price > high_price:
        high_price = price

    avg_price += price

avg_price = round(avg_price / len(nook_inventory), 3)
print('\n')
print('Low Price', low_price, 'bells')
print('High Price', high_price, 'bells')
print('Avg Price', avg_price, 'bells')


# 3 Set up Redd`s counterfeit goods store
def markup(price):
    return math.floor(price + (random.random() * 35))


def discount(price):
    while True:
        discount_price = math.floor(price - (random.random() * 20))
        if discount_price >= 1:
            return discount_price


for item in nook_inventory.keys():
    price = nook_inventory[item]
    nook_or_redd = random.randrange(0, 3)
    if nook_or_redd == 1:
        redd_inventory[item] = markup(price)
    elif nook_or_redd == 2:
        redd_inventory[item] = discount(price)
    else:
        redd_inventory[item] = price

print('\nprice difference from redd')
for item in nook_inventory.keys():
    nook_price = nook_inventory[item]
    redd_price = redd_inventory[item]
    print('[{}]: {}'.format(item, nook_price - redd_price))


# 4 Compare your store`s sales with Redd`s store sales
def random_item(inventory):
    items = list(inventory.keys())
    random_index = math.floor(random.random() * len(items))
    key = items[random_index]
    return { key : inventory[key] }


nook_customers = []
redd_customers = []
item_count = len(nook_inventory)

while True:
    buy_item_count = 0
    input_item_count = input('\nHow many items did the customers buy?(Number of items:{}) '.format(item_count))

    if 'stop' == input_item_count:
        break
    elif int(input_item_count) > item_count:
        print('Your input exceeds number of items registered.')
        continue
    else:
        buy_item_count = int(input_item_count)

    for i in range(buy_item_count):
        nook_or_redd = random.randrange(0, 2)
        if nook_or_redd == 0:
            nook_customers.append(random_item(nook_inventory))
        else:
            redd_customers.append(random_item(redd_inventory))

def print_sell_items(customers):
    total_price = 0
    for sell_item in customers:
        item = list(sell_item.keys())[0]
        total_price += list(sell_item.values())[0]
        print('[{}] Sold'.format(item))
    print('Total earned: {}bell'.format(total_price))
    return total_price


print('\n--- Nook Customers ---')
nook_total = print_sell_items(nook_customers)

print('\n--- Redd Customers ---')
redd_total = print_sell_items(redd_customers)

if nook_total > redd_total:
    print('\nNook`s Cranny made more money')
elif nook_total < redd_total:
    print('\nRedd made more money')
else:
    print('\nThey made the same amount')


# 5 BONUS: Compare specific items from both stores
def distinct_item(customers):
    result = set()
    for sell_item in customers:
        result.add(list(sell_item.keys())[0])
    return result


nook_sell_item_list = distinct_item(nook_customers)
redd_sell_item_list = distinct_item(redd_customers)


def difference(a, b):
    return a.difference(b)


nook_only_sell = difference(nook_sell_item_list, redd_sell_item_list)
redd_only_sell = difference(redd_sell_item_list, nook_sell_item_list)


if nook_sell_item_list == redd_sell_item_list:
    print('\nBoth stores sold the same goods')
elif redd_only_sell.issubset(nook_only_sell):
    print('\nNook`s Cranny sold all the goods sold by Redd and more')
    for item in nook_sell_item_list:
        print(item)
else:
    print('\nWhat Redd sold that Nook`s Cranny didn`t')
    for item in redd_only_sell:
        print(item)



'''
keys function: https://www.geeksforgeeks.org/python-dictionary-keys-method/#:~:text=keys()%20method%20in%20Python,the%20keys%20in%20the%20dictionary.&text=Parameters%3A%20There%20are%20no%20parameters,the%20changes%20in%20the%20dictionary.
issubet method:https://www.w3schools.com/python/ref_set_issubset.asp
'''
