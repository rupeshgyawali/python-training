# import requests
# from bs4 import BeautifulSoup

# response = requests.get('http://www.nepalstock.com/')
# response = requests.get('https://www.daraz.com.np/smartphones/samsung-brand/')

# soup = BeautifulSoup(response.content, 'html.parser')

# print(soup.find('div', class_='pdp-mod-product-price'))

# nepse_stats = soup.find(id='nepse-stats')
# market_watch = nepse_stats.find(id='market-watch')
# market_info = nepse_stats.contents[-2]

# print(market_info.table)

# print(soup.table)
# print(soup.findAll('img'))
