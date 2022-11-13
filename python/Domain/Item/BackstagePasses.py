from Domain.Item.GRItem import GRItem

class BackstagePasses(GRItem):

    def updateQuality(self):
        degradationRate = 1
        if self.sell_in <= 10 and self.sell_in > 5:
            degradationRate = degradationRate * 2
        elif self.sell_in <= 5 and self.sell_in >= 0:
            degradationRate = degradationRate * 3
        self.quality = self.quality + degradationRate
        
        if self.sell_in < 0:
            self.quality = 0
        
        self.checkQuality()