from Domain.Item.GRItem import GRItem

class AgedBrie(GRItem):

    def updateQuality(self):
        self.quality = self.quality+1
        self.checkQuality()