# coding:utf-8
from bs4 import BeautifulSoup
import requests

cookies = {
    'za': 'zhujie',
    'zp': '0fd047d476d752d405da3ef2adb4699638d6394d',
    'zentaosid': '8vopsimpss4nec5p2pen42ceg4'
}

url = 'http://emmsvn.jianq.com:8080/zentao/bug-browse-1--unclosed-0--240-100-1.html'
re = requests.get(url, cookies=cookies)
recontent = re.content
print(re.text)
soup = BeautifulSoup(recontent, 'html.parser')
# text_class = soup.find_all(class_="text-left")
text_class = soup.find_all(class_="text-center")

j = 1
for i in text_class:
    # i_str = ''.join(i.a.string)
    i_title = i.find_all('td')[3].a.string
    print(i.find_all('td')[3]['title'])
    i_name = i.find_all('td')[5].string
    i_bytes = bytes(str(j) +'. ' + i_title + ' ' + i_name + '\n\n', encoding="utf-8")
    #print(type(i_str))
    with open('bug.txt', 'ab') as f:
        f.write(i_bytes)
    j += 1
print('写入成功------')

# text_class = soup.find_all(class_="text-center")
# print(text_class[0].find_all('td')[3].a.string)
# print(text_class[0].find_all('td')[5].string)





