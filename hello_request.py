__author__ = 'dubu'
import requests
r = requests.get('https://api.github.com/events')
r.text
