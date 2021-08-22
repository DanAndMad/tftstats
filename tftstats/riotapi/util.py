from requests.api import post, put, get
from dotenv import load_dotenv
import os
from rest_framework import status

from rest_framework.response import Response

load_dotenv()

TOKEN = os.environ.get('RIOT_API_TOKEN')

BASE_URL_LEAGUE = 'https://na1.api.riotgames.com/tft/league/v1/'
BASE_URL_SUMMONER = 'https://na1.api.riotgames.com/tft/summoner/v1/'
BASE_URL_MATCH = 'https://americas.api.riotgames.com/tft/match/v1/'

def get_league(tier, division, page):
    response = get(BASE_URL_LEAGUE + 'entries/'+ tier + '/' + division + '?api_key=' + TOKEN + '&page=' + page)

    try:
        return response.json()
    except:
        return {'Error': 'Issue with request'}

def get_league_upper(league):
    response = get(BASE_URL_LEAGUE + league + '?api_key=' + TOKEN)

    try: 
        return response.json()
    except:
        return {'Error': 'Issue with request'}

def get_matches(league):
    response = get_league_upper(league)

    if 'Error' in response or 'entries' not in response:
        return {'Error': 'Issue with request'}

    summoner_ids = response.get('entries')[:10]
    summoner_ids = map(lambda summoner: summoner['summonerId'], summoner_ids)

    puuids = []

    for sid in summoner_ids:
        response = get(BASE_URL_SUMMONER + 'summoners' + '/' + sid + '?api_key=' + TOKEN).json()
        puuids.append(response.get('puuid'))

    matches = []

    for pid in puuids:
        response = get(BASE_URL_MATCH + 'matches' + '/' + 'by-puuid' + '/' + pid + '/' + 'ids' + '?count=20' + '&api_key=' + TOKEN).json()
        matches = matches + response

    units = []

    for match in matches:
        response = get(BASE_URL_MATCH + 'matches' + '/' + match + '?api_key=' + TOKEN).json()
        if "info" not in response:
            print(response)
        participants = response.get('info').get('participants')
        match_units = [x.get('units') for x in participants]
        units.append(match_units)

    return {"units": units}

