from vk_api.keyboard import VkKeyboard, VkKeyboardColor

class KB:
    
    @staticmethod
    def board(keyboard_type):
        if(keyboard_type == "main"):
            return KB.get_main()
        elif(keyboard_type == "null"):
            return None
    
    @staticmethod
    def get_main():
        keyboard = VkKeyboard(one_time=True)
        keyboard.add_button('Помощь', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Удар', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Левелап', color=VkKeyboardColor.DEFAULT)
        return keyboard