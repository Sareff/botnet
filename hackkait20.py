from bs4 import BeautifulSoup
from requests import *
import json
import re

s = Session()

URL = "http://dist.kait20.ru/login/index.php"
p = {"index":0,"methodname":"core_fetch_notifications","args":{"contextid":1}}

r = s.get(url = URL)

data = r.text
soup = BeautifulSoup(data, 'html.parser')
inputs = soup.find("input", {"name":"logintoken"})
token = inputs.get('value')

data = {'anchor': '',
        'logintoken': token,
        'username': 'mpavlova',
        'password': 'u1xr0Bh8E0'}

r = s.post(url = URL, data = data)

ans = BeautifulSoup(r.text, 'html.parser')
print(ans)
pattern = re.compile(r"M.cfg = (\{.*?});", re.MULTILINE | re.DOTALL)
script = ans.find("script", text=pattern)
obj = {}

if script:
    obj = pattern.search(script.text).group(1)
    obj = json.loads(obj)

print(obj["sesskey"])


