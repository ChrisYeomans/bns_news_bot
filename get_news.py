#! usr/bin/env python3
import sys, requests, bs4, datetime, to_md

def main():
	tmp = get_news()
	if tmp:
		print(tmp[0])
	else:
		print("no news returned")

def get_news():
	page = requests.get("https://www.bladeandsoul.com/uk/news/")
	soup = bs4.BeautifulSoup(page.text, 'html.parser')
	news_article_list = soup.find(class_="news-article-list").find_all('a')
	date_list = soup.find(class_="news-article-list").find_all('span')

	for a in news_article_list:
		link = "https://www.bladeandsoul.com"+a['href']
		date_posted = a.find('span').get_text().split('|')[0].split(',')[0].strip()
		if date_posted == datetime.datetime.now().strftime("%B") + str(datetime.datetime.now().day):
			return [extract_news(link), link]
		else:
			return []

def extract_news(link):
	page = requests.get(link)
	soup = bs4.BeautifulSoup(page.text, 'html.parser')
	article_html = soup.select(".article")[0]
	article = ' '.join(str(article_html.encode(sys.stdout.encoding, errors='ignore')).split('\n')).replace('\\n', " ").strip().split('\'')[1].replace('*', '')
	md = to_md.convert(article)

	return(md)

if __name__ == "__main__":
	main()