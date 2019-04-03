
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as UReq

flip_url = 'https://www.flipkart.com/search?q=mi%20phone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

scrpurl = UReq(flip_url)
scraphtml = scrpurl.read()
print(type(scraphtml))
scrpurl.close()
# print(scraphtml)
html_dom = soup(scraphtml, 'html.parser')
# print(html_dom)
print(type(html_dom))
phone_list = html_dom.find_all('div', {'class':'_1-2Iqu row'})
print(type(phone_list))
print(len(phone_list))

for phone_names in phone_list:
    phone_name = phone_names.find_all('div', {'class':'_3wU53n'})
    print(phone_name[0].text)
    rating = phone_names.find_all('div', {'class':'hGSR34'})
    print(rating[0].text)
    price = phone_names.find_all('div', {'class':'_1vC4OE _2rQ-NK'})
    print(price[0].text)
    print('------------------')



phone_list_1 = phone_list[0]
# print(phone_list_1)
print(type(phone_list_1))
phone_name = phone_list_1.find_all('div', {'class':'_3wU53n'})
print(phone_name[0].text)
rating = phone_list_1.find_all('div', {'class':'hGSR34'})
print(rating[0].text)
# phone_name = phone_list.find_all('div', {'class':'_3wU53n'})
# print(type(phone_name))

# Formated string f'url'
# split('') string