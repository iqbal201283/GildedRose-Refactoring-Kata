class BaseItemUpdater:
    def __init__(self, item):
        self.item = item

    def update(self):
        self.update_sell_in()
        self.update_quality()

    def update_sell_in(self):
        self.item.sell_in -= 1

    def update_quality(self):
        degrade = 1
        if self.item.sell_in < 0:
            degrade = 2
        self.item.quality = max(self.item.quality - degrade, 0)