import re

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEvent, VkBotEventType

from user import User
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
    

def match_command(command, text):
    result = re.search("@?.*{}".format(command), text)
    return not result == None

def levelup(user):
    level = user.level
    cost = 3*level
    points = user.points
    if(points >= cost):
        user.points -= cost
        user.level += 1
        VK.send_message("Вы повысили свой уровень за {} очков. Теперь у вас {} уровень".format(cost, level+1), user.peer_id, "main")
    else:
        VK.send_message("У вас недостаточно очков для левелапа, для повышения уровня нужно {} очков.".format(cost), user.peer_id, "main")
    user.set_data()

def punch(user):
    user.points += user.level
    VK.send_message("Вы нанесли удар. Ваши очки - {}".format(user.points), user.peer_id, "main")
    user.set_data()

def start(user):
    VK.send_message("""Здравствуйте, {}. 
                       У вас {} очков и {} уровень.

                       Текущие доступные для выполнения команды:
                       Помощь - вызывает справку.
                       Удар - вы ударите.
                       Левелап - увеличить уровень.""".format(user.name, user.points, user.level), user.peer_id, "main")

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