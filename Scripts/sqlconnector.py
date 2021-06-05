from sqlalchemy import create_engine, MetaData

from Resources.template.table_template import Base


class sqliteConnector:

    def __init__(self):
        self.engine = create_engine('sqlite:///Resources/database/cyclone.db')

    def create_tables(self):
        Base.metadata.create_all(self.engine)


def create_tables():
    connector = sqliteConnector()
    connector.create_tables()