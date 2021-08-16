# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class QuotesPipeline:

    def __init__(self):
        self.create_table()
        self.create_database()

    def create_table(self):
        self.conn = sqlite3.connect('mydata.db')
        self.curr = self.conn.cursor()

    def create_database(self):
        self.curr.execute('''DROP TABLE IF EXISTS quotes_db''')
        self.curr.execute(
            '''
                CREATE TABLE quotes_db
                    (text TEXT, author TEXT, tags TEXT)
            '''
        )

    def store_db(self, item):
        text = item['quote'][0]
        author = item['author'][0]
        tags = item['tags'][0]

        self.curr.execute(
            '''INSERT INTO quotes_db VALUES (?, ?, ?)''',
            (text, author, tags)
        )
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item
