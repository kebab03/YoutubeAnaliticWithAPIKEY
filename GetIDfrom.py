import os
import googleapiclient.discovery
# WORKS------------------------------------------------------------------------
# Set up the YouTube Data API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey="AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68")

# Define the video ID
#video_id = "th5_9woFJmk"   @ this is for corey schafer
video_id = "AUTvd2m41Fc"

# Make a request to the videos.list endpoint to get the video details
videos_response = youtube.videos().list(
    part="snippet",
    id=video_id
).execute()

# Extract the channel ID from the video details
channel_id = videos_response["items"][0]["snippet"]["channelId"]

# Print the channel ID
print(channel_id)
