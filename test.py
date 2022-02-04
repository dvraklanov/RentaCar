from database import Database


if __name__ == '__main__':
    db = Database("test_db")
    print(db.insert(table='vehicles', cols=('name', 'spec', 'class'), values=('car', 'str', 'none')))
