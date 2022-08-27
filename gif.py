import requests
import numpy
import json
import os


def get_gif(keywords):
    response = requests.get(
        'https://tenor.googleapis.com/v2/search?q=%s&key=%s' % (keywords, os.getenv('TENOR_KEY')))
    if response.status_code == 200:
        json_raw_data = json.loads(response.text)
    else:
        print('Something went wrong.')
    index = numpy.random.uniform(0, len(json_raw_data['results']))
    gif = json_raw_data['results'][int(index)]['url']
    desc = json_raw_data['results'][int(index)]['content_description']
    return [gif, desc]
