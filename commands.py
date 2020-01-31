import re
from my_vk_api import VK
from user import User

class CM:
    @staticmethod
    def read_command(text, user):
        if(CM.match_command("ПОМОЩЬ", text)):
            CM.start(user)
        elif(CM.match_command("УДАР", text)):
            CM.punch(user)
        elif(CM.match_command("НАЧАТЬ", text)):
            CM.start(user)
        elif(CM.match_command("ЛЕВЕЛАП", text)):
            CM.levelup(user)

    @staticmethod
    def match_command(command, text):
        result = re.search("@?.*{}".format(command), text)
        return not result == None
    
    @staticmethod
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

    @staticmethod
    def punch(user):
        user.points += user.level
        VK.send_message("Вы нанесли удар. Ваши очки - {}".format(user.points), user.peer_id, "main")
        user.set_data()
    
    @staticmethod
    def start(user):
        VK.send_message("""Здравствуйте, {}. 
                           У вас {} очков и {} уровень.

                           Текущие доступные для выполнения команды:
                           Помощь - вызывает справку.
                           Удар - вы ударите.
                           Левелап - увеличить уровень.""".format(user.name, user.points, user.level), user.peer_id, "main")