from bs4 import BeautifulSoup as bs
import requests

url = 'http://ethans_fake_twitter_site.surge.sh/'
response = requests.get(url, timeout=5)
content = bs(response.content, "html.parser")
print(type(content))
#tweet = content.findAll('p', attrs={"class": "content"}).text
#test = content.find_all('p', attrs={"class": "content"})
for tweet in content.find_all('p', attrs={"class": "content"}):
    print(tweet.text.encode('utf-8'))
    
