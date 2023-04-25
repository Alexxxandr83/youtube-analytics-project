import os
import google.auth
from googleapiclient.discovery import build

# ID канала
channel_id = "ucmcgom8gzkhp8zj6l7_hiua"

# API-ключ
api_key = os.environ.get("API-KEY")

# Создание объекта YouTube API
credentials, _ = google.auth.default(scopes=["https://www.googleapis.com/auth/youtube.readonly"])
youtube = build("youtube", "v3", credentials=credentials, developerKey=api_key)

# Выполнение запроса к YouTube API
channel = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id).execute()

# Вывод информации о канале в формате JSON
print(channel)