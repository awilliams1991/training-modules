def bark(name, weight):
    if weight > 20:
        print(name, 'says WOOF WOOF')
    elif weight <= 20 and weight >= 2:
        print(name, 'says woof woof')
    elif weight < 2:
        print(name, 'says yip yip')


bark('Codie', 40)
bark('Sparky', 9)
bark('Jackson', 12)
bark('Fido', 65)
bark('Scottie', -1)
bark('Speedy', 20)
