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
        links[j] = a[j]["href"]

    champs[i] = links

print "<html>\n<title>Championship Series</title>\n<body>"
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\"/>"
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"design.css\"/>"
print "<base href=\"http://basketball-reference.com\">"
print "<base target=\"_blank\" href=\"http://basketball-reference.com\">"
print "</head>"
for i in years:
    print "<p id=\"" + i + "\" ><a href=\"" + baseurl1 + i + ".html\"><br>" + i + "<br></p>"
    print "<table id=\"teams\">"
    print "<tr>"
    for j in champs[i]:
        url = base + j
        team = BeautifulSoup(urllib2.urlopen(url))
        title = team.title.findAll(text=True)[0]
        title = title.split(' ')
        title.pop(0)
        team_name = ""
        for word in title:
            if word != 'Roster':
                team_name = team_name + word +  " "
            else:
                break

        print "<td id=\"team_name\"><a href=\"" + j + "\" align=\"center\"><b>" + team_name + "</b></a></td>"
    print "</tr>"
    print "<tr>"
    for j in champs[i]:
        print "<td id=\"no-outline\">"
        url = base + j
        soup = BeautifulSoup(urllib2.urlopen(url))
        table = soup.findAll("table")[4]
        print table
        print "</td>"
    print "</tr>"
    print "</table>"
print "</body>\n</html>"
