from src.video import Video
import os

if __name__ == '__main__':
    api_key = os.getenv('YT_API_KEY')
    broken_video = Video('broken_video_id', api_key)

    assert broken_video.title is None
    assert broken_video.like_count is None


