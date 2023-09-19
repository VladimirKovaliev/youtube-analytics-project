from src.channel import Channel
import os
if __name__ == '__main__':
    # Создаем два экземпляра класса
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'
    api_key = os.getenv('YT_API_KEY')
    moscowpython = Channel(channel_id, api_key)
    highload = Channel('UCwHL6WHUarjGfUM_586me8w', api_key)

    # Используем различные магические методы
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscowpython + highload)  # 100100
    print(moscowpython - highload)  # -48300
    print(highload - moscowpython)  # 48300
    print(moscowpython > highload)  # False
    print(moscowpython >= highload)  # False
    print(moscowpython < highload)  # True
    print(moscowpython <= highload)  # True
    print(moscowpython == highload)  # False
    
