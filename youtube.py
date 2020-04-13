from selenium import webdriver
import pandas as pd
import csv
from  datetime import datetime
from time import sleep
from youtube_api import YouTubeDataAPI
def look_new_video():
    driver = webdriver.Firefox(executable_path='Webdriver location')
    api_key = 'Get your API key from google'
    channel_id = 'Youtuber channel id'
    base_video_url = 'https://www.youtube.com/watch?v='
    yt = YouTubeDataAPI(api_key)
    youtuber = yt.search(channel_id=channel_id,max_results=30,order_by=('date'))
    videos_title,videos_id = [],[]
    for i in youtuber:
        videos_title.append(i['video_title'])
        videos_id.append(i['video_id'])

    videos_id_check = videos_id[0]

    video_details = pd.DataFrame({
        'video_title': videos_title,
        'video_id': videos_id
        })
    video_details.to_csv('video.csv')
    with open('video.csv','r') as r_file:
        data = csv.reader(r_file)
        for i in data:
            if i[-1] == videos_id_check:
                driver.get(base_video_url+ videos_id_check)
    
try:
    while True:
        look_new_video()
        sleep(8)
except KeyboardInterrupt:
    print("Stopping")
        
