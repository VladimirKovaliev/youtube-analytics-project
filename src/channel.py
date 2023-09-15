from pprint import pprint

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, api_key: str) -> None:
        """Экземпляр инициализируется id канала и api_key. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        response = self.youtube.channels().list(
            part='snippet,statistics',
            id=self.channel_id
        ).execute()
        pprint(response)
