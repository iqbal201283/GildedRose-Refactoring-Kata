class AgedBrieUpdater(BaseItemUpdater):
    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
        if self.item.sell_in < 0 and self.item.quality < 50:
            self.item.quality += 1