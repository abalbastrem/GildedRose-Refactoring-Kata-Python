from Domain.Item.Item import Item

class GRItem(Item):
    def __init__(self, name, sell_in, quality, conjured = False):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.conjured = conjured

    def updateQuality(self):
        degradationRate = 1
        if self.sell_in <= 0:
            degradationRate = degradationRate * 2
        if self.conjured:
            degradationRate = degradationRate * 2
        self.quality = self.quality - degradationRate
        self.checkQuality()

    def checkQuality(self):
        if self.quality < 0:
            self.quality = 0
        if self.quality > 50:
            self.quality = 50

    def updateSellIn(self):
        self.sell_in = self.sell_in - 1