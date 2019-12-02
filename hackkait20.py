from bs4 import BeautifulSoup
from requests import *

URL = "http://dist.kait20.ru/login/index.php"
p = {"index":0,"methodname":"core_fetch_notifications","args":{"contextid":1}}

r = get(url = URL)

data = r.text
soup = BeautifulSoup(data, 'html.parser')
inputs = soup.find("input", {"name":"logintoken"})
print(inputs.get('value'))

