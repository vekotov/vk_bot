import sqlite3
from database import DataBase
from my_vk_api import VK

class User:
    def __init__(self, id):
        self.id = id
        self.peer_id = 0
        self.name = ""
        self.level = 0
        self.points = 0
        self.get_data()
        
    def get_data(self):
        if(not DataBase.id_exist(self.id)):
            DataBase.create_id(self.id)
        self.level = DataBase.get_data(self.id, 'level')
        self.points = DataBase.get_data(self.id, 'points')
        self.name = VK.get_name(self.id)
    
    def set_data(self):
        if(not DataBase.id_exist(self.id)):
            DataBase.create_id(self.id)
        DataBase.set_data(self.id, 'level', self.level)
        DataBase.set_data(self.id, 'points', self.points)