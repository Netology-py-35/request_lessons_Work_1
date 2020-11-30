#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
import json


def get_data(name):
    url = f'https://superheroapi.com/api/2619421814940190/search/{name}'
    r = requests.get(url)
    s = r.json()
    a = json.dumps(s)
    with open(f'heroes_{name}.json', 'a') as f:
        f.write(a + '\n')


def get_json_bag_of_words(json_file):
    with open(json_file, 'r') as file:
        news = json.loads(file.read())
    word_items = news['rss']['channel']['items']
    bag_of_words = []
    for item in word_items:
        bag_of_words.extend(item['description'].split(' '))
    return bag_of_words


def get_intelligence(name):
    with open(f'heroes_{name}.json', 'r') as f:
        heroes = json.loads(f.read())
        hero = heroes['results'][0]['name']
        intelligence = heroes['results'][0]['powerstats']['intelligence']
    return hero, intelligence


if __name__ == '__main__':
    heroes = ['Hulk', 'Captain_America', 'Thanos']
    h = {}
    for hero in heroes:
        h.update({get_intelligence(hero)[0]: get_intelligence(hero)[1]})
        s = sorted(h.items(), key=lambda item: item[1])
    print(f'Самый умный {s[0][0]}, у него {s[0][1]} intelligence')
