import time

import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEvent, VkBotEventType

from keyboards import KB

class VK:
    @staticmethod
    def start_api(token):
        VK.api = vk_api.VkApi(token=token)

    @staticmethod
    def send_message(message, peer_id, keyboard_type):
        keyboard = KB.board(keyboard_type)
        VK.api.method(
            'messages.send',
            {
                'peer_id': peer_id,
                'message': message,
                'random_id': time.time(),
                'keyboard': keyboard if keyboard == None else keyboard.get_keyboard()
            }
        )
    
    @staticmethod
    def get_name(id):
        data = VK.api.method(
            'users.get',
            {
                'user_ids': id
            }
        )
        name = data[0].get('first_name')
        return name
    
    @staticmethod
    def get_event_peer(event):
        return event.object['message']['peer_id']