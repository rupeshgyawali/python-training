from requests_html import HTMLSession
import csv

csv_file = open('products.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Name', 'Price'])

session = HTMLSession()


# response = session.get(
#     '''https://www.daraz.com.np/products/samsung-galaxy-f22-sm-e225f-quad-camera-48mp-94mm-thickness-6000-mah-i105964871-s1027901218.html''')

# response.html.render()
# price = response.html.find('.pdp-mod-product-price', first=True).text
# print(price)


def fetch_and_read(url):
    response = session.get(url)
    response.html.render()
    lst_div = response.html.find('.c1_t2i', first=True)

    for itm_div in lst_div.find('.c2prKC'):
        csv_writer.writerow([itm_div.find(
            '.c16H9d', first=True).text, itm_div.find('.c3gUW0', first=True).text])

    return response


response = fetch_and_read(
    'https://www.daraz.com.np/smartphones/samsung-brand/')

pages = len(response.html.find('ul.ant-pagination', first=True).find('li')) - 3
for i in range(pages):
    fetch_and_read(
        'https://www.daraz.com.np/smartphones/samsung-brand/?page='+str(i+2))

csv_file.close()
