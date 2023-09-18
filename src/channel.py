from pprint import pprint

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, api_key: str) -> None:
        """Экземпляр инициализируется id канала и api_key. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
    @property
    def title(self):
        return self._get_data()['items'][0]['snippet']['title']
    @property
    def channel_id(self):
        return self.channel_id

    @property
    def channel_description(self):
        return self._get_data()['items'][0]['snippet']['description']

    @property
    def url(self):
        return self._get_data()['items'][0]['snippet']['customUrl']

    @property
    def subscribers_count(self):
        return self._get_data()['items'][0]['statistics']['subscriberCount']

    @property
    def video_count(self):
        return self._get_data()['items'][0]['statistics']['videoCount']
    @property
    def views_count(self):
        return self._get_data()['items'][0]['statistics']['viewCount']
    def _get_data(self) -> dict:
        """Метод для получения данных о канале по API."""
        return self.youtube.channels().list(
            part='snippet,statistics',
            id=self.id
        ).execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        response = self.youtube.channels().list(
            part='snippet,statistics',
            id=self.id
        ).execute()
        pprint(response)

