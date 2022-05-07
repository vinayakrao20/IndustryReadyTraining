# 13 A milk vendor buys milk at the rate of 3.25/lt then adds a litre of water for every 4 litres 
# of milk and sells the water milk at the rate of 4.15/lt. Calculate the gain for milk vendor.

pure_milk = 3.25 
water_milk = 3.25*(4+1) # beacuse he is adding 1 ltr for every 4 ltr
selling_price = 4.15*(4+1)
profit = selling_price - water_milk
print(f' Profit for selling 5ltr milk is {profit} and for 1 ltr is {profit/5}') # p/5 for profit in 1 ltr 