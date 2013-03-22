from bs4 import BeautifulSoup
import urllib2

years = [0] * 66
for i in range(0, 66):
    years[i] = str(2012 - i)

baseurl1 = "http://www.basketball-reference.com/leagues/NBA_"
baseurl2 = "http://www.basketball-reference.com/leagues/BAA_"
base = "http://www.basketball-reference.com"
theurl = baseurl1
champs = {}
url = baseurl1
teams = [[""] * 2] * 66
for i in years:
    i = str(i)
    if(int(i) == 1949):
        theurl = baseurl2
    url = theurl + i + ".html"
    soup = BeautifulSoup(urllib2.urlopen(url))
    if(int(i) > 1970):
        table = soup.findAll("table")[3]
    else:
        table = soup.findAll("table")[2]

    td = table.findAll("td")[1]
    a = td.findAll("a")
    links = [""] * 2
    for j in range(0, 2):
    #teams[2012 - int(i)] = [a[j].innerHtml, a[j]["href"]]
        links[j] = a[j]["href"]

    champs[i] = links
    #print teams

print "<html>\n<title>Championship Series</title>\n<body>"
print "<head>\n<script style=\"text/css\">"
print "p {font-size:36px;}"
print "</script>"
print "</head>"
for i in years:
    print "<p align=\"center\">" + i + "<br></p>"
    print "<table>"
    print "<tr>"
    for j in champs[i]:
        print "<td align=\"center\"><b>" + j + "</b></td>"
    print "</tr>"
    print "<tr>"
    for j in champs[i]:
        print "<td>"
        url = base + j
        soup = BeautifulSoup(urllib2.urlopen(url))
        table = soup.findAll("table")[4]
        print table
        print "</td>"
    print "</tr>"
    print "</table>"
print "</body>\n</html>"

