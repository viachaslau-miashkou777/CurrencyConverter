# #Currency converter. Option 1.
# def converter(amount, currency1, currency2, rate, direction):
#     return f'{amount} {currency1} = {round(amount * rate ** direction, 2)} {currency2}'
#
# if __name__ == "__main__":
#     convertion_result1 = converter(1, "USD", "Yuan", 6.81, 1)
#     print(convertion_result1)

#     convertion_result2 = converter(1, "Yuan", "USD", 6.81, -1)
#     print(convertion_result2)

# #Currency converter. Option 2.
# def converter(amount, currency1, currency2, rate, direction):
#     return f'{amount} {currency1} = {round(amount * rate ** direction, 2)} {currency2}'
#
# if __name__ == "__main__":
#     a = 1
#     c1 = "USD"
#     c2 = 'Yuan'
#     r = 6.81
#     d = 1
#     result1 = converter(a, c1, c2, r, d)
#     print(result1)
#
#     a = 1
#     c2 = "USD"
#     c1 = 'Yuan'
#     r = 6.81
#     d = -1
#     result2 = converter(a, c1, c2, r, d)
#     print(result2)

#Currency converter. Option 3.
# def converter(amount, currency1, currency2, rate, direction):
#     return f'{amount} {currency1} = {round(amount * rate ** direction, 2)} {currency2}'
#
# if __name__ == "__main__":
#     a_list = [1, 1, 1500, 1750, 25000, 28000]
#     c1 = "USD"
#     c2 = 'Yuan'
#     r = 6.81
#     d = 1
#     for i in range(0, 5, 2):
#         result1 = converter(a_list[i], c1, c2, r, d)
#         print(result1)
#     for i in range(1, 6, 2):
#         result2 = converter(a_list[i], c2, c1, r, -d)
#         print(result2)

# Currency Converter. Option 4.

from datetime import datetime
current_date = datetime.now().date()
currency_list = ['usd', 'yuan']
rate = 6.81
currency_to_buy = ''
while currency_to_buy not in currency_list:
    currency_to_buy = input(
        f' we can suggest {currency_list[0]} or {currency_list[1]} to exchange, please, choose the currency: ')
if currency_to_buy == currency_list[0]:
    print(f'we sell {currency_list[0]} for {currency_list[1]}')
else:
    print(f'we sell {currency_list[1]} for {currency_list[0]}')
while 1!=0:
    amount = input('enter the amount you want to buy: ')
    try:
        float(amount)
        break
    except ValueError:
        continue
if currency_to_buy == currency_list[0]:
    print(current_date, f'exchange rate is: {round(rate, 3)}, your amount to sell in {currency_list[1]} is: ',
          round(float(amount)*rate, 2))
else:
    print(current_date, f'exchange rate is: {round(1/rate, 3)}, your amount to sell in {currency_list[0]} is: ',
          round(float(amount)/rate, 2))
