import time
print(int(time.time()))





print("Hello Trixie_LM")

print("Pinkie Pie")


class Purse:

    def __init__(self, valuta, name='Unknown'):
        self.money = 0.00
        self.valuta = valuta
        self.name = name

    def top_up_balance(self, quantity):
        self.money = self.money + quantity

    def info(self):
        print(self.money)



x = Purse('USD')
y = Purse('RUB', 'Apple')

x.top_up_balance(100)
x.info()
