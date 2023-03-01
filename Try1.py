from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# Set up the API client
api_key = "AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68"
youtube = build("youtube", "v3", developerKey=api_key)

# Set the channel ID
channel_id = "UCCezIgC97PvUuR4_gbFUs5g"

# Set the search parameters
search_params = {
    "channelId": channel_id,
    "type": "video",
    "part": "id,snippet",
    "maxResults": 50
}

try:
    # Call the search.list method to retrieve the list of videos for the channel
    search_response = youtube.search().list(**search_params).execute()

    # Extract the video details from the search response
    videos = []
    for item in search_response["items"]:
        video = {
            "title": item["snippet"]["title"],
            "video_id": item["id"]["videoId"],
            "view_count": 0
        }
        videos.append(video)

    # Call the videos.list method to retrieve the view count for each video
    for i in range(0, len(videos), 50):
        video_ids = [v["video_id"] for v in videos[i:i+50]]
        video_params = {
            "id": ",".join(video_ids),
            "part": "statistics"
        }
        video_response = youtube.videos().list(**video_params).execute()

        # Update the view count for each video
        for item in video_response["items"]:
            for video in videos:
                if video["video_id"] == item["id"]:
                    video["view_count"] = int(item["statistics"]["viewCount"])

    # Sort the videos by view count in descending order
    sorted_videos = sorted(videos, key=lambda v: v["view_count"], reverse=True)

    # Print the video titles and view counts
    for video in sorted_videos:
        print(f"{video['title']} - {video['view_count']} views")

except HttpError as error:
    print(f"An HTTP error occurred: {error}")
