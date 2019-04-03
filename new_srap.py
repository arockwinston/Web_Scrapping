from lxml import *
from bs4 import BeautifulSoup as soup, CData
import requests
'''
wiki = requests.get('https://en.wikipedia.org/wiki/Ball').text
wikihtml = soup(wiki, 'lxml')

wikipara = wikihtml.find('div', class_='mw-content-ltr')
print(type(wikipara.b.string))
wp = wikipara.find_all('p')
for ancher in wp[2].find_all('a'):
    if ancher['title'] == 'Rubber':
        str = ancher.text
        # print(str.replace_with('Dupper'))
        # ancher.tag.replace_with('Dupper')

    val = 'https://en.wikipedia.org{}'.format(ancher['href'])
    print(val)
'''
with open('sample.html') as sam:
    html = soup(sam, 'lxml')
    print(html.name)

    bold = html.find('div').b
    # print(type(bold))
    bold.name = 'em'
    # print(bold.attrs)
    # print(bold.get_attribute_list('class'))
    # print(bold['class'][0])
    bold.i.string.replace_with('Arock')
    # print(bold.children)
    print(bold.contents)
    print("----------")
    for child in bold.children:
        print(child)
    para = html.find('div').p
    print("----------")
    print(para)
    print(para.children)
    print("----------")
    for child in para.children:
        print(type(child))


    if len(para.contents) == 1 and para.contents[0] == '\n':
        print('got it')


    # print(bold.replace_with('Arock'))



# with open('sample.htm') as sample:
#     html = soup(sample, 'lxml')
#     paravalue = html.find_all('p')
#     for p in paravalue:
#         print(p.text)
