from bs4 import BeautifulSoup
import urllib2

year = [0] * 66
for i in range(0, 66):
    year[i] = str(2012 - i)

baseurl1 = "http://www.basketball-reference.com/leagues/NBA_"
baseurl2 = "http://www.basketball-reference.com/leagues/BAA_"

champs = {}
url = baseurl1
for i in year:
    if(int(i) == 1949):
        print 'changing'
        url = baseurl2
    i = str(i)
    url = url + i + ".html"
    soup = BeautifulSoup(urllib2.urlopen(url))
    if(int(i) > 1970):
        table = soup.findAll("table")[3]
    else:
        table = soup.findAll("table")[2]

    td = table.findAll("td")[1]
    a = td.findAll("a")
    links = [""] * 2
    for j in range(0, 2):
        links[j] = a[j]["href"]

    print "\n\n" + i
    for k in links:
        print "\t" + k

