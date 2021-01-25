# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from sqlalchemy.orm import sessionmaker
from scrapy.exceptions import DropItem
from news_mk.models import News , create_table , db_connect
from news_mk.items import NewsMkItem


class NewsMkPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker
        Creates tables
        """
        engine = db_connect()
        create_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        news = News()
        news.title = item["title"]
        news.data = item["data"]
        news.url = item["url"]

        # exist_title = session.query(News).filter_by(title = news.title).first()
        # if exist_title is not None:  # the current url exists
        #     news.title = exist_title
        # else:
        #     news.title = news

        
        try:
            session.add(news)
            session.commit()

        except:
            session.rollback()
            raise

        finally:
            session.close()
        
        return item
