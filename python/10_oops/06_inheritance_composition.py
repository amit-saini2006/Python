class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai...")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardomom, ginger, cloves.")

class ChaiShop:
    chai_Cls = BaseChai

    def __init__(self):
        self.chai = self.chai_Cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type}  chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_Cls = MasalaChai

shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()