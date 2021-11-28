from django.db import models

class Elements(models.Model):
    px = models.FloatField()
    qty = models.FloatField()
    num = models.IntegerField()
    value = models.FloatField()

    class Meta:
        abstract = True

class L3BTCUSDBids(Elements):
    class Meta:
        verbose_name = 'L3BT-USD Bid'
        verbose_name_plural = 'L3BT-USD Bids'

    def to_dict(self):
        return {
            'px': round(self.px, 2),
            'qty': round(self.qty, 2),
            'num': round(self.num, 2),
            'value': round(self.value, 2),
        }

class L3BTCUSDAsks(Elements):
    class Meta:
        verbose_name = 'L3BT-USD Ask'
        verbose_name_plural = 'L3BT-USD Asks'

    def to_dict(self):
        return {
            'px': round(self.px, 2),
            'qty': round(self.qty, 2),
            'num': round(self.num, 2),
            'value': round(self.value, 2),
        }
