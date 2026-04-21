menu = ['Croissant','Banana','Coffee','Cinamon bun' ]


stock = {menu[0]:3, menu[1]:5, menu[2]:2, menu[3]:4}

price = {menu[0]:1.95, menu[1]:1.5, menu[2]:5, menu[3]:6}
total = 0

for item in menu:
    Value_stock = float(stock[item])*float(price[item])
    total += Value_stock


print(total)