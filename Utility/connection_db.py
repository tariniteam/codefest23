from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class DBconn:
    Session = None

    def __init__(self):
        self.engine = create_engine("mssql+pyodbc://tarini_root:gravitY0@tarini-therapy.database.windows.net/TariniDB?driver=ODBC+Driver+18+for+SQL+Server")
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def get_session(self):
        return self.session
