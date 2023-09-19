from pprint import pprint
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str, api_key: str) -> None:
        """Экземпляр инициализируется id канала и api_key. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)
    def __str__(self):
        return f'{self.title}, https://www.youtube.com/channel/{self.id}'

    def __add__(self, other):
        return int(self.subscribers_count) + int(other.subscribers_count)
    def __sub__(self, other):
        return int(self.subscribers_count) - int(other.subscribers_count)
    def __gt__(self, other):
        return int(self.subscribers_count) > int(other.subscribers_count)
    def __ge__(self, other):
        return int(self.subscribers_count) >= int(other.subscribers_count)
    @property
    def title(self):
        return self._get_data()['items'][0]['snippet']['title']
    @property
    def channel_id(self):
        return {self.channel_id}

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

    @classmethod
    def get_service(cls):
        """Метод для получения объекта для работы с YouTube API."""
        return build('youtube', 'v3', developerKey='your_developer_key')


    def to_json(self, filename):
        """Метод для сохранения значений атрибутов экземпляра в файл json."""
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.channel_description,
            'url': self.url,
            'subscriber_count': self.subscribers_count,
            'video_count': self.video_count,
            'view_count': self.views_count,
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)