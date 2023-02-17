#Currency Converter. Option 4.
# (a) Write a program that converts USD to Yuan and Yuan's to USD.
# (b) Use your program to convert amount in USD to Yuan's
# 1 USD to Yuan
# 1500 USD to Yuan
# 25000 USD to Yuan
# (c) Use your program to convert amount in USD to Yuan's
# 1 Yuan to USD
# 1750 Yuan to USD
# 28000 Yuan to USD
# (d) Display conversion results on the screen, before printing out the conversion results, remember to display the date and the currency exchange rate.

from datetime import datetime
current_date = datetime.now().date()
def converter(amount, currency1, currency2, rate, direction):
    return f'{amount} {currency1} = {round(amount * rate ** direction, 2)} {currency2}'

if __name__ == "__main__":
    a_list = [1, 1, 1500, 1750, 25000, 28000]
    c1 = "USD"
    c2 = 'Yuan'
    ex_rate = 6.87
    d = 1
    print(current_date, f'exchange rate is: {ex_rate}')
    for i in range(0, 5, 2):
        result1 = converter(a_list[i], c1, c2, ex_rate, d)
        print( result1)
    for i in range(1, 6, 2):
        result2 = converter(a_list[i], c2, c1, ex_rate, -d)
        print(result2)

