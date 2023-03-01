from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the API client
#api_key = "YOUR_API_KEY"
api_key="AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68"
youtube = build("youtube", "v3", developerKey=api_key)

# Replace CHANNEL_ID with the ID of the channel you want to get the most viewed video from
#channel_id = "CHANNEL_ID"
#channel_id = 'UCbXgNpp0jedKWcQiULLbDTA'
channel_id = "UCCezIgC97PvUuR4_gbFUs5g"
try:
    # Get the channel's uploads playlist ID
    channels_response = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    ).execute()

    uploads_playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Get all of the videos from the uploads playlist
    playlistitems_response = youtube.playlistItems().list(
        part="snippet,statistics",
        playlistId=uploads_playlist_id,
        maxResults=50
    ).execute()

    playlist_items = playlistitems_response["items"]

    # Sort the videos by view count in descending order
    sorted_videos = sorted(playlist_items, key=lambda x: int(x["statistics"]["viewCount"]), reverse=True)

    most_viewed_video = sorted_videos[0]["snippet"]["title"]
    most_viewed_video_id = sorted_videos[0]["snippet"]["resourceId"]["videoId"]

    print(f"The most viewed video is '{most_viewed_video}', with the ID '{most_viewed_video_id}'")

except HttpError as error:
    print("An HTTP error occurred:")
    print(error)