import requests
from bs4 import BeautifulSoup as bfs

def get_url(url):
    for n in range(220, 750):
        dir_url = url + format(n) + "/"
        r = requests.get(dir_url).content
        soup = bfs(r, "html.parser")
        div = soup.find("div", {"id" : "wallwindow"})
        imgs = div.findChildren()
        for img in imgs:
            src = img.get('src')
            if (not "WP_" in src):
                continue
            else:
                print src

get_url("http://www.justinmaller.com/wallpaper/")
