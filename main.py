import urllib.request
from bs4 import BeautifulSoup
from urllib.error import HTTPError

f1 = open("results", "w+")
f2 = open("targets", "r")

for line in f2:
    line = line.replace("\n", "")
    res = ''
    try:
        html_doc = urllib.request.urlopen('https://www.youtube.com/'+line+'/about')
        soup = BeautifulSoup(html_doc, 'html.parser')
        for s in soup.find_all("span", "about-stat"):
            t = s.find("b")
            if t:
                ft = t.string
                ft = ft.strip().replace(" ", "")
                if len(ft) > 0:
                    res += ft + ", "
        if len(res) > 3:
            res = res[:-2]
            f1.write(res+"\n")
            print("Data for user was added: "+line)
        else:
            f1.write("0, 0\n")
            print("Can not add data for next line: "+line)
    except HTTPError:
        f1.write("Was removed, Was removed\n")
        print("Channel was removed.")
            

f1.write(res)
f1.close()
f2.close()