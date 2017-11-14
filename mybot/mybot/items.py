import scrapy
from scrapy_djangoitem import DjangoItem
#from scrapy_djangoitem import Field
from myapp.models import Person


class PersonItem(DjangoItem):
    django_model = Person
    #sex = scrapy.Field()