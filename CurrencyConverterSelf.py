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

