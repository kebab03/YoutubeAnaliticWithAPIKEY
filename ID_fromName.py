from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
#it works
# WORKS------------------------------------------------------------------------
# Set up the API client
api_key="AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68"
youtube = build("youtube", "v3", developerKey=api_key)

# Replace SHOW_NAME with the name of the channel you want to find the ID for
show_name = "Kebab Sharif"
#show_name = "Corey Schafer"
try:
    # Search for channels with the given show name
    search_response = youtube.search().list(
        q=show_name,
        type="channel",
        part="id,snippet"
    ).execute()

    # Retrieve the channel ID from the search results
    if "items" in search_response:
        channel_id = search_response["items"][0]["id"]["channelId"]
        print(f"The channel ID for {show_name} is {channel_id}")
    else:
        print(f"No channel ID found for {show_name}")

except HttpError as error:
    print("An HTTP error occurred:")
    print(error)