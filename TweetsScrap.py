# user
import tweepy
import time
import json
from datetime import datetime
import re

CONSUMER_KEY = "ENTER YOUR API STUFF"
CONSUMER_SECRET = "ENTER YOUR API STUFF"
ACCESS_TOKEN_KEY = "ENTER YOUR API STUFF"
ACCESS_TOKEN_SECRET = "ENTER YOUR API STUFF"
pattern1 = re.compile(r'(\s){2,}')
pattern2 = re.compile(r'^(\s){1,}')
pattern3 = re.compile(r'(\s)$')
pattern4 = re.compile(r'^RT')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth ,wait_on_rate_limit=True)
trends = api.trends_place(1)

def scrape_tweets(username):
    datalist = []
    user = ""
    print(username)
    tweets = tweepy.Cursor(api.user_timeline, id=username, since_id = the_Tweetsid_of_the_starting_date, max_id = the_Tweetsid_of_the_ending_date, tweet_mode = "extended").items()
    try:
        for tweet in tweets:
            if tweet._json['lang'] != "en":
                continue
            favorite_count = tweet._json["favorite_count"]
            date = tweet._json['created_at'].replace('+0000 ', '')
            date = str(datetime.strptime(date, "%a %b %d %H:%M:%S %Y"))
            user = tweet._json['user']['name']
            id_str = tweet._json["id_str"]
            content = tweet._json["full_text"]
            if re.search(pattern4, content):
                continue
            content = re.sub(pattern1, '\n', content)
            content = re.sub(pattern2, '', content)
            content = re.sub(pattern3, '', content)

            data = dict(count = len(datalist) + 1,  account = user, date = date, id = id_str, favorite_count = favorite_count, content = content)
            datalist.append(data)
            
        return datalist
    except:
        print("error");
#     filename = "{}.json".format(user)
#     with open( filename, 'w', encoding = 'utf-8') as f:
#         json.dump(datalist, f, ensure_ascii=False,indent = 4)

file = 'input.json'
with open(file, 'r', encoding = 'utf-8') as f:
    followers = json.load(f)
x = 0
all_tweets = []
# for x in range(len(followers)):
'''for follower in followers: 
#     if followers[x]["location"]:
    x += 1
#         print(str(x+1) + ": " + followers[x]['location'])
    all_tweets.append(scrape_tweets(follower['account']))
    print("Scraping...")
    print(x)'''
        
with open( "output.json", 'w', encoding = 'utf-8') as f:
    json.dump(all_tweets , f, ensure_ascii=False,indent = 4)

print("Done")

