from pprint import pprint
from googleapiclient.discovery import build

class Video:
    def __init__(self, channel_id: str, api_key: str) -> None:
        """Экземпляр инициализируется id канала и api_key. Дальше все данные будут подтягиваться по API."""
        self.id = channel_id
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def __str__(self):
        return self._get_data()['items'][0]['snippet']['title']

    @property
    def get_id(self):
        return self._get_data()['items'][0]['id']
    def get_title(self):
        return self._get_data()['items'][0]['snippet']['title']
    def get_url(self):
        return f"https://www.youtube.com/watch?v={self.id}"
    def get_views_count(self) -> int:
        return int(self._get_data()['items'][0]['statistics']['viewCount'])
    def get_like_count(self):
        return int(self._get_data()['items'][0]['statistics']['likeCount'])


    def _get_data(self) -> dict:
        """Метод для получения данных о канале по API."""
        return self.youtube.videos().list(
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

class PLVideo(Video):
    """
    Класс для работы с видео в плейлисте на YouTube.
    """
    def __init__(self, video_id: str, playlist_id: str, api_key):
        super().__init__(video_id, api_key)
        self.__playlist_id = playlist_id

    def get_playlist_id(self) -> str:
        return self.__playlist_id
