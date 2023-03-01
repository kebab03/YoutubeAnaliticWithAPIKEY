import googleapiclient.discovery

api_key="AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68"
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

channel_id = "UC-3mnxdBYyxIWc_RGf_sC1A"

response = youtube.channels().list(
    part="snippet",
    id=channel_id
).execute()

channel_name = response['items'][0]['snippet']['title']

print("Channel name:", channel_name)
