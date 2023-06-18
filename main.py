class Human:
    default_name = "No name"
    default_age = 0

    def __init(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name} \nAge: {self.age} \nMoney: {self.__money} \nHouse: {self.__house}")

    @staticmethod
    def default_info(default_name=default_name, default_age=default_age):
        print(f"default_name: {default_name} \ndefault_age: {default_age}")

    def __make_deal(self, small_house_price):  # покупка дома
        self.__money = self.__money - small_house_price
        self.__house = self.__class.house

    def earn_money(self):  # увеличение кол-ва значения денег
        print(f"Earned {1000} money!", end="")
        self.__money = self.__money + 1000
        print(f" Current value {self.__money}")

    def buy_house(self):
        print(f"Final price: {self.__class.house.final_price()}")
        small_house_price = self.__class.house.final_price()
        if self.__money < small_house_price:
            print("Not enough money!")
        else:
            self.__class.make_deal(small_house_price)

class House:
    def __init(self, area=0, price=0):
        self._area = area
        self._price = price

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, value):
        self._area = value

    @property
    def price(self):
        return self.area * 30

class SmallHouse(House):
    def init(self, obj=40):
        super().init(area=obj)

Human.default_info()
Danil = Human("Danil", 25)
Danil.info()
Danil_Home = SmallHouse()
Danil.buy_house()
Danil.earn_money()
Danil.buy_house()
Danil.earn_money()
Danil.buy_house()
Danil.info()
