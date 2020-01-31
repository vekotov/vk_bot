import re

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEvent, VkBotEventType

from user import User
from commands import CM
from my_vk_api import VK
from database import DataBase

DATABASE_NAME = "database.db"


TOKEN = "NONE"
GROUP_ID = 0

def use_event(event):
    #Создаем обьект пользователя имеющий все важные данные о нем
    user_id = event.object['message']['from_id']
    user = User(user_id)
    user.peer_id = event.object['message']['peer_id']

    print("USER ID = {}".format(user.id))
    print("USER LEVEL = {}".format(user.level))
    print("USER POINTS = {}".format(user.points))

    #Определяем запрошенную команду
    text = event.object['message']['text'].upper()
    CM.read_command(text, user)

VK.start_api(TOKEN)
DataBase.startdb(DATABASE_NAME)
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=TOKEN)

# Работа с сообщениями
longpoll = vk_api.bot_longpoll.VkBotLongPoll(vk, GROUP_ID)

# Основной цикл
print("Server started")
for event in longpoll.listen():
    print("{}".format(event))
    if event.type == VkBotEventType.MESSAGE_NEW:
        print("EVENT NEW MESSAGE")
        if event.from_user:
            print("EVENT FROM USER")
            use_event(event)
        elif event.from_chat:
            print("EVENT FROM CHAT")
            use_event(event)