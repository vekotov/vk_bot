import sqlite3

class DataBase:
    @staticmethod
    def startdb(name, default_level=1, default_points=0):
        DataBase.conn = sqlite3.connect(name)
        DataBase.cursor = DataBase.conn.cursor()
        DataBase.cursor.execute("""CREATE TABLE IF NOT EXISTS players(id bigint, points bigint, level bigint)""")
        DataBase.default_level = default_level
        DataBase.default_points = default_points
    
    @staticmethod
    def get_data(id, type):
        if(DataBase.id_exist(id)):
            DataBase.cursor.execute("""SELECT {}
                                       FROM players
                                       WHERE id = {}""".format(type, id))
            result = DataBase.cursor.fetchone()
            print("RESULT = {}".format(result))
            result = result[0]
            print("TYPE {}, VALUE = {}".format(type, result))
            return result
        else:
            return None
    
    @staticmethod
    def set_data(id, type, value):
        DataBase.cursor.execute("""UPDATE players
                                   SET {} = {}
                                   WHERE id = {}""".format(type, value, id))
        DataBase.conn.commit()
    
    @staticmethod
    def create_id(id):
        print("CREATED ID {}".format(id))
        DataBase.cursor.execute("""INSERT INTO players VALUES({}, {}, {})""".format(id, DataBase.default_points, DataBase.default_level))
        DataBase.conn.commit()
    
    @staticmethod
    def id_exist(id):
        DataBase.cursor.execute("""SELECT COUNT(*)
                                   FROM players
                                   WHERE id = ?""", [(id)])
        found_sql = DataBase.cursor.fetchone()
        print("FOUND = {}".format(found_sql))
        found_sql = found_sql[0]
        print("FOUND = {}".format(found_sql))
        return found_sql != 0