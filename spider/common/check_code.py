# coding:utf-8
from PIL import Image
import pytesseract
import requests
from io import StringIO

text = pytesseract.image_to_string(Image.open('1.jpeg'))
print(text)

# def get_check_code():
#     url = 'http://192.168.2.52:8181/emm-api/authorization/checkCode.json?inumber=2'
#     res = requests.post(url)
#     return res
#
# code = get_check_code()
# with open('a.jpg', 'wb') as f:
#     f.write(code.content)
# print(type(code))
# print(code.content)
# f = StringIO.write(code.raw)
# im = Image.open(f)
# im.save('a.jpg')