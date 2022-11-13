# -*- coding: utf-8 -*-
import unittest

from Domain.gilded_rose import GildedRose
from Domain.Item.GRItem import GRItem
from Domain.Item.AgedBrie import AgedBrie
from Domain.Item.Sulfuras import Sulfuras
from Domain.Item.BackstagePasses import BackstagePasses


class GildedRoseTest(unittest.TestCase):

    def testUpdate(self):
        items = [
            GRItem("GR1 Apple", 1, 10),
            GRItem("GR2 Venison meat", -3, 3),
            GRItem("GR3 Talking Banana (Conjured)", 10, 5, True),
            GRItem("GR4 Apple Conjured", -3, 5, True),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("GR1 Apple", items[0].name)
        self.assertEquals(0, items[0].sell_in)
        self.assertEquals(9, items[0].quality)
        self.assertEquals("GR2 Venison meat", items[1].name)
        self.assertEquals(-4, items[1].sell_in)
        self.assertEquals(1, items[1].quality)
        self.assertEquals("GR3 Talking Banana (Conjured)", items[2].name)
        self.assertEquals(9, items[2].sell_in)
        self.assertEquals(3, items[2].quality)
        self.assertEquals("GR4 Apple Conjured", items[3].name)
        self.assertEquals(-4, items[3].sell_in)
        self.assertEquals(1, items[3].quality)

        gilded_rose.update_quality()

        self.assertEquals("GR1 Apple", items[0].name)
        self.assertEquals(7, items[0].quality)
        self.assertEquals("GR2 Venison meat", items[1].name)
        self.assertEquals(0, items[1].quality)
        self.assertEquals("GR3 Talking Banana (Conjured)", items[2].name)
        self.assertEquals(1, items[2].quality)
        self.assertEquals("GR4 Apple Conjured", items[3].name)
        self.assertEquals(0, items[3].quality)

    def testLimitQuality(self):
        items = [
            GRItem("GR1 Apple", 1, -20),
            GRItem("GR2 Venison meat", -3, 300)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("GR1 Apple", items[0].name)
        self.assertEquals(0, items[0].quality)
        self.assertEquals("GR2 Venison meat", items[1].name)
        self.assertEquals(50, items[1].quality)

    def testAgedBrie(self):
        items = [
            AgedBrie("Orgrimmar Brie", 2, 20),
            AgedBrie("Albacete Brie", -5, 20),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(21, items[0].quality)
        self.assertEquals(21, items[1].quality)

    def testSulfuras(self):
        items = [Sulfuras("Sulfuras, Hand of Ragnaros", 99, 99)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEquals(80, items[0].quality)

    def testBackstagePasses(self):
        items = [
            BackstagePasses("BS Passes for Libintia", 11, 10),
            BackstagePasses("BS Passes for Blind Guardian", 10, 10),
            BackstagePasses("BS Passes for Necrogoblikon", 4, 10),
            BackstagePasses("BS Passes for El Fary", 0, 10),
            BackstagePasses("BS Passes for Eleuvetie", -5, 10),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEquals(11, items[0].quality)
        self.assertEquals(12, items[1].quality)
        self.assertEquals(13, items[2].quality)
        self.assertEquals(13, items[3].quality)
        self.assertEquals(0, items[4].quality)



        
if __name__ == '__main__':
    unittest.main()
