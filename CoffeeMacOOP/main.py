MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
class coffeemachine(coffee, price):

    def resourcecontrol(self,coffee):
        for i in resources:
            if coffee[i] > resources[i]:
                print(f"not enough {i}")
                return False
        return True

    def moneycontrol(self):
        total = input("1 Kuruş: ") * 0.01
        toal += input("10 Kuruş: ") * 0.1
        total += input()

