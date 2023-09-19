from django.db import models

class WebsiteCarbonFootprint(models.Model):
    url = models.CharField(max_length=1024)
    is_green = models.BooleanField(default=False, blank=True)
    energy_on_page_load = models.CharField(max_length=128)
    co2_transferred_on_page_load = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.url


class CoffeePicture(models.Model):
    url = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.url