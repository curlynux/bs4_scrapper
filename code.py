import requests
from bs4 import BeautifulSoup as bfs

def get_url(url):
    for n in range(0, 1000):
        dir_url = url + format(n) + "/"
        r = requests.get(dir_url).content
        soup = bfs(r, "html.parser")
        imgs = soup.find("div", {"id" : "wallwindow"}).findChildren()
        for img in imgs:
            src = img.get('src')
            if (not "WP_" in src):
                print "no img in the dir number: %d" % n
            else:
                print "img number: %d, src: %s" % (n, src)

get_url("http://www.justinmaller.com/wallpaper/")
