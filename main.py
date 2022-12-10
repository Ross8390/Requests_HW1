import requests


urls = [
    'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/332.json',
    'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/655.json',
    'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/149.json',
]


def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r



def get_highest_iq():
    super_hero = []
    for item in requests_get(urls):
        intelligence = item.json()
        for power_stats in intelligence:
            super_hero.append({
                'name': intelligence['name'],
                'intelligence': intelligence['powerstats']['intelligence']
            })

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_hero:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный {name}, интелект: {intelligence_super_hero}")


get_highest_iq()