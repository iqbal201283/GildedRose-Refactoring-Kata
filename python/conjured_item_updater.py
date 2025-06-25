class ConjuredItemUpdater(BaseItemUpdater):
    def update_quality(self):
        degrade = 2
        if self.item.sell_in < 0:
            degrade *= 2
        self.item.quality = max(self.item.quality - degrade, 0)