# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime
import dateparser

import scrapy


def convert_date(text):
    text = dateparser.parse(text)
    return text

class NewsMkItem(scrapy.Item):
    # define the fields for your item here like:
    title = Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )
    
    data =  Field(
        input_processor=MapCompose(convert_date),
        output_processor=TakeFirst()
        )
    url =  Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
        )