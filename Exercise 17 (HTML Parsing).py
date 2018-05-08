import requests
from bs4 import BeautifulSoup

url = "https://nytimes.com"
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, "html.parser")
headers = soup.find_all(['h1', 'h2'], { "class" : "story-heading"})

for story_heading in headers:
	print(story_heading.text.strip())
'''   if story_heading.a:
		print(story_heading.a.text.replace("\n", " ").strip())
	else:
		print(story_heading.contents[0].strip())

## filter to only headers with class="story-heading"'''