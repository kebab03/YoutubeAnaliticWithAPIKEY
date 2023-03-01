from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the API client
api_key = "AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68"
youtube = build("youtube", "v3", developerKey=api_key)

# Specify the channel ID
channel_id = "UCCezIgC97PvUuR4_gbFUs5g"

# Retrieve the channel's videos
playlist_items = []
next_page_token = None
while True:
    playlist_response = youtube.playlistItems().list(
        part="snippet",
        playlistId=channel_id,
        maxResults=50,
        pageToken=next_page_token
    ).execute()

    playlist_items += playlist_response["items"]
    next_page_token = playlist_response.get("nextPageToken")

    if next_page_token is None:
        break

# Sort the videos by view count in descending order
sorted_videos = sorted(playlist_items, key=lambda x: int(x["snippet"]["thumbnails"]["default"]["url"].split("/")[4]), reverse=True)

# Print the video title and view count for each video
for video in sorted_videos:
    video_id = video["snippet"]["resourceId"]["videoId"]
    video_title = video["snippet"]["title"]
    video_views = int(video["snippet"]["thumbnails"]["default"]["url"].split("/")[4])
    print(f"{video_title} - {video_views} views")
