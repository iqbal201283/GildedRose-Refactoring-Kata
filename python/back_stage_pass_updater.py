class BackstagePassUpdater(BaseItemUpdater):
    def update_quality(self):
        if self.item.sell_in < 0:
            self.item.quality = 0
        elif self.item.sell_in < 5:
            self.item.quality = min(self.item.quality + 3, 50)
        elif self.item.sell_in < 10:
            self.item.quality = min(self.item.quality + 2, 50)
        else:
            if self.item.quality < 50:
                self.item.quality += 1