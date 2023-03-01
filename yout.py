#from yt_stats import YTstats
from YoutubeStatis import YTstats

python_engineer_id = 'UCbXgNpp0jedKWcQiULLbDTA'
channel_id = python_engineer_id
api_key="AIzaSyBFDE_oZ2V9LItUMvII8tQbk6PwdPthx68"
#yt = YTstats(API_KEY, channel_id)
yt = YTstats(api_key, channel_id)
yt.extract_all()
yt.dump()  # dumps to .json