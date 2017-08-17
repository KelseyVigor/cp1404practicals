'''work out total price for a number of items, each with different prices
    program allows user to enter the number of items and
        the price of each item
program computers and displays the total price
if the total price is over $100, 10% discuount applied to total before print
    if number of items < 0, must display 'invalid number of items!' and prompt user until valid response '''

valid_input = False
while not valid_input:
    number_of_items = int(input("Please enter number of items: "))
    if number_of_items <= 0:
        print("Invalid number of items!")
    else:
        valid_input = True

price_of_items = []
i = 0
while i < number_of_items:
    item_price = float(input("Please enter price of item: "))
    price_of_items.append(item_price)
    i += 1

print("Number of items: ", number_of_items)
i = 0
while i < number_of_items:
    print("Price of item: ${:.2f}".format(price_of_items[i]))
    i +=1

total_price = sum(price_of_items)
if total_price > 100:
    total_price * 0.10
print("Total price for", number_of_items, "items is ${:.2f}".format(total_price))
