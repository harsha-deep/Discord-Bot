import requests
import numpy
import json


def get_meme(subreddit):
    response = requests.get(
        'https://www.reddit.com/r/%s/.json?over_18=%s' % (subreddit, 'false'), headers={'User-agent': 'Xenon'})
    if response.status_code == 200:
        json_raw_data = json.loads(response.text)
    else:
        print('Something went wrong.')
    index = numpy.random.uniform(0, len(json_raw_data['data']['children']))
    meme = json_raw_data['data']['children'][int(index)]['data']['url']
    author = json_raw_data['data']['children'][int(index)]['data']['author']
    title = json_raw_data['data']['children'][int(index)]['data']['title']
    return [meme, author, title]
