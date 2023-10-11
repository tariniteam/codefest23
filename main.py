from Utility import connection_db
from Objects import UserType

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conn = connection_db.DBconn()
    db_session = conn.get_session()

    # UserType.create(db_session, "test", '2022-10-12', 'test2', '2022-10-12', 'test2', '2022-10-12', 'test2', True)
    result = UserType.get(db_session, 1)
    print(result)


