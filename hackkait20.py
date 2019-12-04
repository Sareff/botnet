from bs4 import BeautifulSoup
from requests import *

s = Session()

URL = "http://dist.kait20.ru/login/index.php"

r = s.get(url = URL)

data = r.text
soup = BeautifulSoup(data, 'html.parser')
inputs = soup.find("input", {"name":"logintoken"})
token = inputs.get('value')

print(token)

data = {'anchor': '',
        'logintoken': token,
        'username': 'yuandrejtseva',
        'password': 'YWeTxTQS0P'}

r = s.post(url = URL, data = data)
answer = BeautifulSoup(r.text, 'html.parser')
print(answer)
course = answer.find_all("div", {"id": "page-content-container-2"})
#gid = course.get("data-course-id")
#print(gid)
print(course)

