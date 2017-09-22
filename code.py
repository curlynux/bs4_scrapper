import requests
from bs4 import BeautifulSoup as bfs

url = "http://www.justinmaller.com/wallpaper/"

def get_url():
    arr = {}
    n = 59
    while n <= range(n, 1000):
        dir_url = url + format(n) + "/"
        r = requests.get(dir_url).content
        soup = bfs(r, "html.parser")
        imgs = soup.find("div", {"id" : "wallwindow"}).findChildren()
        n += 1
        for img in imgs:
            src = img.get('src')
            if (not "WP_" in src):
                pass
                #print "no img in the dir number: %d" % n
            else:
                arr[n] = src
                for value in arr:
                    print value, arr[value]

get_url()
