#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup as bfs

url = "http://www.justinmaller.com/wallpaper/"

def get_url():
    arr = {}
    for n in range(59, 1000):
        soup = bfs(requests.get(url + format(n) + "/").content, "html.parser").find("div", {"id" : "wallwindow"}).findChildren()
        for img in soup:
            if (not "WP_" in img.get('src')):pass
            else:
                arr[n] = img.get('src')
                for value in arr: print value, arr[value]

get_url()
