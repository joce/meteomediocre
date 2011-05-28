import urllib2
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen("http://www.meteomedia.com/fourteenday/caab0103?ref=qlink_lt_14day"))

data = soup.find(id="wrap_14day_graph").script.text

days = re.findall('(\d+)', re.search('var days=(.*);', txt).group(1))
months = re.findall('(\w+)', re.search('var months=(.*);', txt).group(1))
highs = re.findall('(\d+)', re.search('var highs=(.*);', txt).group(1))
lows = re.findall('(\d+)', re.search('var lows=(.*);', txt).group(1))
wxcodes = re.findall('(\w)', re.search('var wxcodes=(.*);', txt).group(1))

print(days)