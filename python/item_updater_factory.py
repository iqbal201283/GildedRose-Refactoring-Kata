class ItemUpdaterFactory:
    @staticmethod
    def get_updater(item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater(item)
        elif item.name == "Backstage passes":
            return BackstagePassUpdater(item)
        elif item.name == "Sulfuras":
            return SulfurasUpdater(item)
        else:
            return BaseItemUpdater(item)