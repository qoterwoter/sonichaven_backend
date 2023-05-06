import requests
import json

def get_playcounts(artist_name, track_name):
    api_key = 'c0b058025b3364ce1fe057c8c9c52e01'
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={api_key}&artist={artist_name}&track={track_name}&format=json'
    response = requests.get(url)
    data = json.loads(response.text)
    playcounts = data['track']['playcount']
    return playcounts
