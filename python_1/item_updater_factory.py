from aged_brie_updater import *
from back_stage_pass_updater import *
from base_item_updater import *
from conjured_item_updater import *
from sulfuras_updater import *



class ItemUpdaterFactory:
    @staticmethod
    def get_updater(item):
        if item.name.split(" ") == "Aged":
            return AgedBrieUpdater(item)
        elif item.name.split(" ") == "Backstage":
            return BackstagePassUpdater(item)
        elif item.name.split(",") == "Sulfuras":
            return SulfurasUpdater(item)
        elif item.name.split(" ") == "Conjured":
            return ConjuredItemUpdater(item)
        else:
            return BaseItemUpdater(item)