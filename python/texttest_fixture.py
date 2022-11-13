# -*- coding: utf-8 -*-
from __future__ import print_function

from Domain.gilded_rose import GildedRose
from Domain.Item.AgedBrie import AgedBrie
from Domain.Item.BackstagePasses import BackstagePasses
from Domain.Item.Sulfuras import Sulfuras
from Domain.Item.GRItem import GRItem

if __name__ == "__main__":

    items = [
             GRItem(name="+5 Dexterity Vest", sell_in=10, quality=20),
             AgedBrie(name="Aged Brie", sell_in=2, quality=0),
             GRItem(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Sulfuras(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             BackstagePasses(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             GRItem(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_quality()
