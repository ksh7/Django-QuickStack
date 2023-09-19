import datetime
import requests

from django.utils import timezone
from django.conf import settings
from celery import shared_task

from . import models

CARBON_FOOTPRINT_API = "https://api.websitecarbon.com/site?url="
COFFEE_PICTURE_API = "https://coffee.alexflipnote.dev/random.json"


@shared_task(name="fetch_random_coffee_picture")
def fetch_random_coffee_picture():
    """ Fetches a random coffee image from API, two times every day"""

    r = requests.get(COFFEE_PICTURE_API)
    models.CoffeePicture.objects.create(url=r.json()["file"])
    return True


@shared_task(name="calculate_website_carbon_footprint")
def calculate_website_carbon_footprint(url):
    """ Calculates a given URL's carbon footprint"""

    r = requests.get(CARBON_FOOTPRINT_API + str(url))
    data = r.json()
    if data:
        models.WebsiteCarbonFootprint.objects.create(url=url,
                                                    is_green=False if data['green']=="unknown" else data['green'],
                                                    energy_on_page_load=data['statistics']['energy'],
                                                    co2_transferred_on_page_load=data['statistics']['co2']['grid']['grams'])
    return True


@shared_task(name="add_numbers")
def add_numbers(num1, num2):
    """ Adds two numbers """
    return num1 + num2