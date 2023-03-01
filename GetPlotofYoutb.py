from googleapiclient.discovery import build
from matplotlib import pyplot as plt

api_key = "AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68"
youtube = build("youtube", "v3", developerKey=api_key)

# Set the channel ID and the number of videos you want to retrieve
channel_id = "UCCezIgC97PvUuR4_gbFUs5g"
max_results = 50

# Get the playlist ID for the channel's uploaded videos
channels_response = youtube.channels().list(
    id=channel_id,
    part="contentDetails"
).execute()

uploads_playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

# Retrieve the first 50 videos from the playlist
playlistitems_response = youtube.playlistItems().list(
    playlistId=uploads_playlist_id,
    part="snippet",
    maxResults=max_results
).execute()

# Extract the video IDs and view counts from the playlist items
video_ids = []
view_counts = []
for item in playlistitems_response["items"]:
    video_ids.append(item["snippet"]["resourceId"]["videoId"])
    video_response = youtube.videos().list(
        id=item["snippet"]["resourceId"]["videoId"],
        part="statistics"
    ).execute()
    view_counts.append(int(video_response["items"][0]["statistics"]["viewCount"]))

# Sort the videos by view count
sorted_videos = sorted(zip(video_ids, view_counts), key=lambda x: x[1], reverse=True)

# Extract the video IDs and view counts from the sorted videos
sorted_video_ids = [x[0] for x in sorted_videos]
sorted_view_counts = [x[1] for x in sorted_videos]

# Plot the view counts for the top 50 videos
plt.bar(range(len(sorted_view_counts)), sorted_view_counts)
plt.xlabel("Videos")
plt.ylabel("View Count")
plt.title(f"Top {max_results} videos for channel {channel_id}")
plt.show()
