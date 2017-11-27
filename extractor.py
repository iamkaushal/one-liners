import requests
from lxml import html
import json
import io

oneliners = []
for i in range(1,420):
    print i
    url = "https://onelinefun.com/{}/".format(i)
    r = requests.get(url)
    htmlwa = (r.text)
    tree = html.fromstring(htmlwa)
    p = tree.xpath("//div[@class='oneliner']/p/text()")
    for temp in p:
        oneliners.append(temp)

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

with io.open('data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps({'oneliners' : oneliners}, ensure_ascii=False)
    outfile.write(to_unicode(str_))

# Read JSON file
with open('data.json') as data_file:
    data_loaded = json.load(data_file)

print(oneliners == data_loaded['oneliners'])
